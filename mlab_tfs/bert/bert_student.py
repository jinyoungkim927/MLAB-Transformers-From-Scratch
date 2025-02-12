import math

from einops import rearrange, repeat
import torch as t
from torch import einsum
from torch.nn import functional as F
from torch import nn


def raw_attention_pattern(
    token_activations,  # Tensor[batch_size, seq_length, hidden_size(768)],
    num_heads,
    project_query,      # nn.Module, (Tensor[..., 768]) -> Tensor[..., 768],
    project_key,        # nn.Module, (Tensor[..., 768]) -> Tensor[..., 768]
):  # -> Tensor[batch_size, head_num, key_token: seq_length, query_token: seq_length]:
    raise NotImplementedError


def bert_attention(
    token_activations,  # : Tensor[batch_size, seq_length, hidden_size (768)],
    num_heads: int,
    # : Tensor[batch_size,num_heads, seq_length, seq_length],
    attention_pattern,
    project_value,  # : function( (Tensor[..., 768]) -> Tensor[..., 768] ),
    project_output,  # : function( (Tensor[..., 768]) -> Tensor[..., 768] )
):  # -> Tensor[batch_size, seq_length, hidden_size]
    raise NotImplementedError


class MultiHeadedSelfAttention(nn.Module):
    def __init__(self, num_heads, hidden_size):
        super().__init__()
        raise NotImplementedError

    def forward(self, input):  # b n l
        raise NotImplementedError


def bert_mlp(token_activations,  # : torch.Tensor[batch_size,seq_length,768],
             linear_1: nn.Module, linear_2: nn.Module
             ):  # -> torch.Tensor[batch_size, seq_length, 768]
    raise NotImplementedError


class BertMLP(nn.Module):
    def __init__(self, input_size: int, intermediate_size: int):
        super().__init__()
        raise NotImplementedError

    def forward(self, input):
        raise NotImplementedError


class LayerNorm(nn.Module):
    def __init__(self, normalized_dim: int):
        super().__init__()
        raise NotImplementedError

    def forward(self, input):
        raise NotImplementedError


class BertBlock(nn.Module):
    def __init__(self, hidden_size, intermediate_size, num_heads, dropout: float):
        super().__init__()
        raise NotImplementedError

    def forward(self, input):
        raise NotImplementedError


class Embedding(nn.Module):
    def __init__(self, vocab_size, embed_size):
        super().__init__()
        raise NotImplementedError

    def forward(self, input):
        raise NotImplementedError


def bert_embedding(
    input_ids,  # : [batch, seqlen],
    token_type_ids,  # [batch, seqlen],
    position_embedding,  # : nn.Embedding,
    token_embedding,  # : nn.Embedding,
    token_type_embedding,  # : nn.Embedding,
    layer_norm,  # : nn.Module,
    dropout  # : nn.Module
):
    raise NotImplementedError


class BertEmbedding(nn.Module):
    def __init__(self, vocab_size, hidden_size, max_position_embeddings, type_vocab_size,
                 dropout: float):
        super().__init__()
        raise NotImplementedError

    def forward(self, input_ids, token_type_ids):
        raise NotImplementedError


class Bert(nn.Module):
    def __init__(self, vocab_size, hidden_size, max_position_embeddings, type_vocab_size,
                 dropout, intermediate_size, num_heads, num_layers):
        super().__init__()
        raise NotImplementedError

    def forward(self, input_ids):
        raise NotImplementedError


class BertWithClassify(nn.Module):
    def __init__(self, vocab_size, hidden_size, max_position_embeddings, type_vocab_size,
                 dropout, intermediate_size, num_heads, num_layers, num_classes):
        super().__init__()
        raise NotImplementedError

    def forward(self, input_ids):
        raise NotImplementedError
