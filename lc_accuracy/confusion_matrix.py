import numpy as np
import pandas as pd

def compute_confusion_matrix(y_true, y_pred, labels=None):
    """
    Computes a confusion matrix for two categorical rasters.

    Parameters
    ----------
    y_true : array-like
        Reference (ground truth) raster values.
    y_pred : array-like
        Predicted raster values.
    labels : array-like, optional
        List of class labels to enforce consistent ordering.

    Returns
    -------
    pandas.DataFrame
        Confusion matrix (rows = reference, columns = predicted).
    """
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()

    if labels is None:
        labels = np.unique(np.concatenate([y_true, y_pred]))

    cm = np.zeros((len(labels), len(labels)), dtype=int)
    label_to_index = {label: idx for idx, label in enumerate(labels)}

    for t, p in zip(y_true, y_pred):
        cm[label_to_index[t], label_to_index[p]] += 1

    return pd.DataFrame(cm, index=labels, columns=labels)