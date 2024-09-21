import unittest
import torch
from torch import Tensor

class SegSum:
    def __init__(self, sequence_length, device):
        self.sequence_length = sequence_length
        self.device = device
        self.mask_excl_diag = self.build_mask_excl_diag()
        self.mask_incl_diag = self.build_mask_incl_diag()

    def build_mask_excl_diag(self):
        return torch.tril(
            torch.ones(self.sequence_length, self.sequence_length, device=self.device, dtype=torch.bool),
            diagonal=-1
        )

    def build_mask_incl_diag(self):
        return torch.tril(
            torch.ones(self.sequence_length, self.sequence_length, device=self.device, dtype=torch.bool),
            diagonal=0
        )

    def segsum(self, input_tensor: Tensor) -> Tensor:
        # Ensure input_tensor has the expected sequence length
        if input_tensor.size(-1) != self.sequence_length:
            raise ValueError("Input tensor's sequence length does not match the precomputed masks.")

        # Expand input_tensor
        input_tensor = input_tensor.unsqueeze(-1).expand(*input_tensor.shape, self.sequence_length)

        # Reshape masks for broadcasting
        dims = [1] * (input_tensor.dim() - 2) + [self.sequence_length, self.sequence_length]
        mask_excl_diag = self.mask_excl_diag.view(*dims)
        mask_incl_diag = self.mask_incl_diag.view(*dims)

        # Apply first mask
        input_tensor = input_tensor.masked_fill(~mask_excl_diag, 0)

        # Compute cumulative sum
        x_segsum = torch.cumsum(input_tensor, dim=-2)

        # Apply second mask
        x_segsum = x_segsum.masked_fill(~mask_incl_diag, -torch.inf)

        return x_segsum

class TestSegsum(unittest.TestCase):
    def assertTensorAllClose(self, x: Tensor, y: Tensor, rtol=1e-5, atol=1e-8):
        self.assertTrue(
            torch.allclose(x, y, rtol=rtol, atol=atol, equal_nan=True),
            f"Tensors are not all close:\nx = {x}\ny = {y}"
        )

    def test_segsum_1d(self):
        x = torch.tensor([1.0, 2.0, 3.0])
        expected = torch.tensor([
            [0.0, -torch.inf, -torch.inf],
            [2.0, 0.0, -torch.inf],
            [5.0, 3.0, 0.0]
        ])
        device = x.device
        sequence_length = x.size(-1)
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        self.assertTensorAllClose(result, expected)

    def test_segsum_2d(self):
        x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
        expected = torch.tensor([
            [[0.0, -torch.inf], [2.0, 0.0]],
            [[0.0, -torch.inf], [4.0, 0.0]]
        ])
        device = x.device
        sequence_length = x.size(-1)
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        self.assertTensorAllClose(result, expected)

    def test_segsum_with_batch(self):
        x = torch.tensor([
            [[1.0, 2.0], [3.0, 4.0]],
            [[5.0, 6.0], [7.0, 8.0]]
        ])
        expected = torch.tensor([
            [[[0.0, -torch.inf], [2.0, 0.0]], [[0.0, -torch.inf], [4.0, 0.0]]],
            [[[0.0, -torch.inf], [6.0, 0.0]], [[0.0, -torch.inf], [8.0, 0.0]]]
        ])
        device = x.device
        sequence_length = x.size(-1)
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        self.assertTensorAllClose(result, expected)

    def test_segsum_larger_sequence(self):
        x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
        expected = torch.tensor([
            [0.0, -torch.inf, -torch.inf, -torch.inf, -torch.inf],
            [2.0, 0.0, -torch.inf, -torch.inf, -torch.inf],
            [5.0, 3.0, 0.0, -torch.inf, -torch.inf],
            [9.0, 7.0, 4.0, 0.0, -torch.inf],
            [14.0, 12.0, 9.0, 5.0, 0.0]
        ])
        device = x.device
        sequence_length = x.size(-1)
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        self.assertTensorAllClose(result, expected)

    def test_segsum_float(self):
        x = torch.tensor([0.1, 0.2, 0.3])
        expected = torch.tensor([
            [0.0, -torch.inf, -torch.inf],
            [0.2, 0.0, -torch.inf],
            [0.5, 0.3, 0.0]
        ])
        device = x.device
        sequence_length = x.size(-1)
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        self.assertTensorAllClose(result, expected)

    def test_segsum_negative(self):
        x = torch.tensor([-1.0, 2.0, -3.0])
        expected = torch.tensor([
            [0.0, -torch.inf, -torch.inf],
            [2.0, 0.0, -torch.inf],
            [-1.0, -3.0, 0.0]
        ])
        device = x.device
        sequence_length = x.size(-1)
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        self.assertTensorAllClose(result, expected)

    def test_segsum_empty(self):
        x = torch.tensor([])
        device = x.device
        sequence_length = x.size(-1) if x.dim() > 0 else 0
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        self.assertEqual(result.shape, (0, 0))

    def test_segsum_single_element(self):
        x = torch.tensor([5.0])
        expected = torch.tensor([[0.0]])
        device = x.device
        sequence_length = x.size(-1)
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        self.assertTensorAllClose(result, expected)

    def test_segsum_high_dimensional(self):
        """Test segsum with a 4D input tensor."""
        x = torch.rand(2, 3, 4, 5)
        device = x.device
        sequence_length = x.size(-1)
        segsum_instance = SegSum(sequence_length, device)
        result = segsum_instance.segsum(x)
        expected_shape = (2, 3, 4, 5, 5)
        self.assertEqual(result.shape, expected_shape)
