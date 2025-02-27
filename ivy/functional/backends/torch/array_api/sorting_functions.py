# global
import torch
from typing import Union, Optional, Tuple, List


def argsort(x: torch.Tensor,
            axis: int = -1,
            descending: bool = False,
            stable: bool = True)\
            -> torch.Tensor:
    return torch.argsort(x, dim=axis, descending=descending)
