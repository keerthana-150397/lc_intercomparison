import sys
import os

# Make sure the main module is importable
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import numpy as np
import pandas as pd

from lc_intercomparison_full import (
    compute_confusion_matrix,
    overall_accuracy,
    kappa_coefficient,
    producers_accuracy,
    users_accuracy
)

# --------------------------------------------------
# Confusion matrix test
# --------------------------------------------------
def test_confusion_matrix_basic():
    y_true = [0, 0, 1, 1, 2, 2]
    y_pred = [0, 1, 1, 1, 2, 0]

    cm = compute_confusion_matrix(y_true, y_pred)

    expected = pd.DataFrame(
        [[1, 1, 0],
         [0, 2, 0],
         [1, 0, 1]],
        index=[0, 1, 2],
        columns=[0, 1, 2]
    )

    pd.testing.assert_frame_equal(cm, expected)


# --------------------------------------------------
# Overall accuracy test
# --------------------------------------------------
def test_overall_accuracy():
    cm = pd.DataFrame(
        [[5, 1],
         [2, 6]],
        index=[0, 1],
        columns=[0, 1]
    )

    oa = overall_accuracy(cm)
    expected_oa = (5 + 6) / (5 + 1 + 2 + 6)

    assert np.isclose(oa, expected_oa)


# --------------------------------------------------
# Kappa coefficient test
# --------------------------------------------------
def test_kappa_coefficient():
    cm = pd.DataFrame(
        [[40, 10],
         [5, 45]],
        index=[0, 1],
        columns=[0, 1]
    )

    total = cm.values.sum()
    po = (40 + 45) / total

    row_marg = cm.sum(axis=1).values
    col_marg = cm.sum(axis=0).values
    pe = np.sum(row_marg * col_marg) / (total ** 2)

    expected_kappa = (po - pe) / (1 - pe)

    kappa = kappa_coefficient(cm)

    assert np.isclose(kappa, expected_kappa)


# --------------------------------------------------
# Producer's Accuracy test
# --------------------------------------------------
def test_producers_accuracy():
    cm = pd.DataFrame(
        [[8, 2],
         [1, 9]],
        index=[0, 1],
        columns=[0, 1]
    )

    pa = producers_accuracy(cm)

    expected_pa = np.array([
        8 / (8 + 2),
        9 / (1 + 9)
    ])

    assert np.allclose(pa, expected_pa)


# --------------------------------------------------
# User's Accuracy test
# --------------------------------------------------
def test_users_accuracy():
    cm = pd.DataFrame(
        [[8, 2],
         [1, 9]],
        index=[0, 1],
        columns=[0, 1]
    )

    ua = users_accuracy(cm)

    expected_ua = np.array([
        8 / (8 + 1),
        9 / (2 + 9)
    ])

    assert np.allclose(ua, expected_ua)


print("✅ All tests passed successfully!")
