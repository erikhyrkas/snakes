from torch import nn

from ys.language_model.attention_block import AttentionBlock
from ys.language_model.config import Config


class AttentionBlocks(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.attention_layers = nn.ModuleList([AttentionBlock(config) for _ in range(config.num_layers)])


    def forward(self, embedded_input):
        for attention in self.attention_layers:
            embedded_input = attention(embedded_input)
        return embedded_input