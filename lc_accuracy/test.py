import numpy as np
import pandas as pd

from confusion_matrix import compute_confusion_matrix
from accuracy_metrics import (
    overall_accuracy,
    kappa_coefficient,
    producers_accuracy,
    users_accuracy
)

# --------------------------------------------------
# Synthetic test data
# --------------------------------------------------

def create_test_arrays():
    """
    Creates small synthetic reference and predicted arrays
    with known expected results.
    """
    y_true = np.array([
        1, 1, 1, 2, 2, 3
    ])

    y_pred = np.array([
        1, 2, 1, 2, 3, 3
    ])

    return y_true, y_pred


# --------------------------------------------------
# Test confusion matrix
# --------------------------------------------------

def test_confusion_matrix():
    y_true, y_pred = create_test_arrays()
    cm = compute_confusion_matrix(y_true, y_pred)

    expected = pd.DataFrame(
        [[2, 1, 0],
         [0, 1, 1],
         [0, 0, 1]],
        index=[1, 2, 3],
        columns=[1, 2, 3]
    )

    assert cm.equals(expected), "Confusion matrix values are incorrect"


# --------------------------------------------------
# Test overall accuracy
# --------------------------------------------------

def test_overall_accuracy():
    y_true, y_pred = create_test_arrays()
    cm = compute_confusion_matrix(y_true, y_pred)

    oa = overall_accuracy(cm)
    expected_oa = 4 / 6  # 4 correct out of 6 pixels

    assert np.isclose(oa, expected_oa), "Overall accuracy calculation failed"


# --------------------------------------------------
# Test kappa coefficient
# --------------------------------------------------

def test_kappa_coefficient():
    y_true, y_pred = create_test_arrays()
    cm = compute_confusion_matrix(y_true, y_pred)

    kappa = kappa_coefficient(cm)
    expected_kappa = 0.5

    assert np.isclose(kappa, expected_kappa, atol=1e-6), \
        "Kappa coefficient calculation failed"



# --------------------------------------------------
# Test Producer’s Accuracy
# --------------------------------------------------

def test_producers_accuracy():
    y_true, y_pred = create_test_arrays()
    cm = compute_confusion_matrix(y_true, y_pred)

    pa = producers_accuracy(cm)
    expected_pa = np.array([
        2 / 3,  # class 1
        1 / 2,  # class 2
        1 / 1   # class 3
    ])

    assert np.allclose(pa, expected_pa), \
        "Producer’s accuracy calculation failed"


# --------------------------------------------------
# Test User’s Accuracy
# --------------------------------------------------

def test_users_accuracy():
    y_true, y_pred = create_test_arrays()
    cm = compute_confusion_matrix(y_true, y_pred)

    ua = users_accuracy(cm)
    expected_ua = np.array([
        2 / 2,  # class 1
        1 / 2,  # class 2
        1 / 2   # class 3
    ])

    assert np.allclose(ua, expected_ua), \
        "User’s accuracy calculation failed"


# --------------------------------------------------
# Run tests manually
# --------------------------------------------------

if __name__ == "__main__":
    test_confusion_matrix()
    test_overall_accuracy()
    test_kappa_coefficient()
    test_producers_accuracy()
    test_users_accuracy()

    print("✅ All tests passed successfully!")
