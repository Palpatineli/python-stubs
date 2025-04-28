from typing import Any, Literal
import os
import numpy as np
import numpy.typing as npt
from nibabel import Nifti1Image

def load(filename: os.PathLike[str]) -> Nifti1Image: ...

def save(img: Nifti1Image, filename: os.PathLike[str]): ...

class Nifti1Image:
    affine: np.ndarray[tuple[Literal[4], Literal[4]], np.dtype[np.float_]]

    def get_fdata(self, caching: Literal['fill', 'unchanged'] = 'fill',
                  dtype: npt.DTypeLike = np.float64) -> np.ndarray[Any, np.dtype[np.floating]]: ...
