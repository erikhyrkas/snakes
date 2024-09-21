import unittest
import torch
from torch.testing import assert_close


def segsum(x):
    """Reimplementation of segment sum calculation without einops."""
    T = x.size(-2)  # Sequence length
    D = x.size(-1)  # Embedding dimension

    # Expand the tensor by adding a new dimension and repeating it along sequence length
    x_expanded = x.unsqueeze(-2).expand(x.size(0), T, T, D)

    # Create a lower-triangular mask to allow summing only current and past elements
    mask = torch.tril(torch.ones(T, T, device=x.device, dtype=torch.bool), diagonal=0)

    # Apply the mask to limit summation
    x_masked = x_expanded.masked_fill(~mask.unsqueeze(0).unsqueeze(-1), 0)

    # Compute the cumulative sum along the sequence dimension
    x_segsum = torch.cumsum(x_masked, dim=-2)

    # Apply mask again to ensure future steps are set to -inf
    x_segsum = x_segsum.masked_fill(~mask.unsqueeze(0).unsqueeze(-1), float('-inf'))

    return x_segsum




class TestSegsum(unittest.TestCase):
    def test_basic_functionality(self):
        x = torch.tensor([[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]])
        result = segsum(x)
        expected = torch.tensor([[[[1.0000, 2.0000],  # Step 1: Cumsum of itself
                                   [4.0000, 6.0000],  # Step 2: Cumsum with previous steps
                                   [9.0000, 12.0000]],  # Step 3: Cumsum with all past steps
                                  [[float('-inf'), float('-inf')],  # Masked out, no previous values
                                   [3.0000, 4.0000],  # Step 2: Cumsum of itself
                                   [8.0000, 10.0000]],  # Step 3: Cumsum with previous steps
                                  [[float('-inf'), float('-inf')],
                                   [float('-inf'), float('-inf')],
                                   [5.0000, 6.0000]]]])  # Last step: Cumsum of itself
        assert_close(result, expected, equal_nan=True)

    def test_zero_tensor(self):
        x = torch.zeros((2, 3, 4))  # All zeros
        result = segsum(x)
        expected = torch.zeros((2, 3, 3, 4))
        expected[:, :, 1:, :] = float('-inf')  # Mask out future steps with -inf
        assert_close(result, expected, equal_nan=True)

    def test_single_element(self):
        x = torch.tensor([[[1.0]]])
        result = segsum(x)
        expected = torch.tensor([[[[1.0]]]])
        assert_close(result, expected)

    def test_large_tensor(self):
        x = torch.randn(5, 100, 64)
        result = segsum(x)
        self.assertEqual(result.shape, (5, 100, 100, 64))

    def test_negative_values(self):
        x = torch.tensor([[[-1.0, -2.0], [-3.0, -4.0], [-5.0, -6.0]]])
        result = segsum(x)
        expected = torch.tensor([[[[-1.0000, -2.0000],  # Step 1: Cumsum of itself
                                   [-4.0000, -6.0000],  # Step 2: Cumsum with previous steps
                                   [-9.0000, -12.0000]],  # Step 3: Cumsum with all past steps
                                  [[float('-inf'), float('-inf')],  # Masked out
                                   [-3.0000, -4.0000],  # Step 2: Cumsum of itself
                                   [-8.0000, -10.0000]],  # Step 3: Cumsum with previous steps
                                  [[float('-inf'), float('-inf')],
                                   [float('-inf'), float('-inf')],
                                   [-5.0000, -6.0000]]]])  # Last step: Cumsum of itself
        assert_close(result, expected, equal_nan=True)

    def test_device_consistency(self):
        if torch.cuda.is_available():
            x = torch.randn(2, 3, 4).cuda()
            result = segsum(x)
            self.assertTrue(result.is_cuda)
            self.assertEqual(result.device, x.device)
