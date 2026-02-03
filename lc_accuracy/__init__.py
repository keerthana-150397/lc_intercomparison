"""
lc_accuracy

A Python package for land-cover map intercomparison and accuracy assessment.

This package provides utilities for:
- Confusion matrix computation
- Accuracy metrics (OA, Kappa, PA, UA)
- Raster loading for categorical land cover datasets

Developed as part of a PhD-level Geospatial Processing course.
"""

from .utils import (
    compute_confusion_matrix,
    overall_accuracy,
    kappa_coefficient,
    producers_accuracy,
    users_accuracy,
    load_raster
)

__all__ = [
    "compute_confusion_matrix",
    "overall_accuracy",
    "kappa_coefficient",
    "producers_accuracy",
    "users_accuracy",
    "load_raster",
]
