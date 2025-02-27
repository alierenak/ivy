# global
import torch
from torch import Tensor
from typing import Union, Tuple, Optional

# local
from ivy import dtype_from_str, default_dtype, dev_from_str, default_device


# noinspection PyShadowingName
def zeros(shape: Union[int, Tuple[int, ...]],
          dtype: Optional[torch.dtype] = None,
          device: Optional[torch.device] = None) \
        -> Tensor:
    return torch.zeros(shape, dtype=dtype_from_str(default_dtype(dtype)), device=dev_from_str(default_device(device)))


def ones(shape: Union[int, Tuple[int, ...]],
         dtype: Optional[torch.dtype] = None,
         device: Optional[Union[torch.device, str]] = None) \
        -> torch.Tensor:
    dtype_val: torch.dtype = ivy.dtype_from_str(dtype)
    dev = ivy.default_device(device)
    return torch.ones(shape, dtype=dtype_val, device=ivy.dev_from_str(dev))
