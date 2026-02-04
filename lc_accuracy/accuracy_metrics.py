import numpy as np

def overall_accuracy(confusion_matrix):
    """
    Computes Overall Accuracy (OA).
    """
    cm = confusion_matrix.values
    return np.trace(cm) / cm.sum()


def kappa_coefficient(confusion_matrix):
    """
    Computes Cohen's Kappa coefficient.
    """
    cm = confusion_matrix.values
    total = cm.sum()

    po = np.trace(cm) / total
    row_marginals = cm.sum(axis=1)
    col_marginals = cm.sum(axis=0)
    pe = np.sum(row_marginals * col_marginals) / (total ** 2)

    return (po - pe) / (1 - pe)


def producers_accuracy(confusion_matrix):
    """
    Computes Producer's Accuracy (PA) for each class.
    """
    cm = confusion_matrix.values
    correct = np.diag(cm)
    reference_total = cm.sum(axis=1)

    return correct / reference_total


def users_accuracy(confusion_matrix):
    """
    Computes User's Accuracy (UA) for each class.
    """
    cm = confusion_matrix.values
    correct = np.diag(cm)
    classified_total = cm.sum(axis=0)

    return correct / classified_total