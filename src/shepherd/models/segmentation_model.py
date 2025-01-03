"""
Segmentation model.
"""

from abc import abstractmethod
from typing import List

import numpy as np

from .base_model import BaseModel


class SegmentationModel(BaseModel):
    """
    Base class for segmentation models.
    """

    def __init__(self, model_path: str, device: str):
        super().__init__(model_path, device)

    @abstractmethod
    def segment(self, image: np.ndarray) -> List[np.ndarray]:
        """
        Segment objects in image.
        Returns list of segmentation masks.
        """
