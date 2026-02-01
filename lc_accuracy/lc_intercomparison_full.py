

import numpy as np 
import pandas as pd
import rasterio
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------------------------
# Confusion matrix
# --------------------------------------------------
def compute_confusion_matrix(y_true, y_pred, labels=None):
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()

    if labels is None:
        labels = np.unique(np.concatenate([y_true, y_pred]))

    cm = np.zeros((len(labels), len(labels)), dtype=int)
    label_to_index = {label: idx for idx, label in enumerate(labels)}

    for t, p in zip(y_true, y_pred):
        cm[label_to_index[t], label_to_index[p]] += 1

    return pd.DataFrame(cm, index=labels, columns=labels)


# --------------------------------------------------
# Accuracy metrics
# --------------------------------------------------
def overall_accuracy(confusion_matrix):
    cm = confusion_matrix.values
    return np.trace(cm) / cm.sum()


def kappa_coefficient(confusion_matrix):
    cm = confusion_matrix.values
    total = cm.sum()
    po = np.trace(cm) / total
    row_marginals = cm.sum(axis=1)
    col_marginals = cm.sum(axis=0)
    pe = np.sum(row_marginals * col_marginals) / (total ** 2)
    return (po - pe) / (1 - pe)


def producers_accuracy(confusion_matrix):
    cm = confusion_matrix.values
    correct = np.diag(cm)
    reference_total = cm.sum(axis=1)
    return correct / reference_total


def users_accuracy(confusion_matrix):
    cm = confusion_matrix.values
    correct = np.diag(cm)
    classified_total = cm.sum(axis=0)
    return correct / classified_total


# --------------------------------------------------
# Raster loader
# --------------------------------------------------
def load_raster(path):
    with rasterio.open(path) as src:
        return src.read(1)


# --------------------------------------------------
# MAIN
# --------------------------------------------------
if __name__ == "__main__":

    # ----------------------------
    # Input paths
    # ----------------------------
    cci_path = r"C:\Users\user\OneDrive - Politecnico di Milano\00GLANCE_Forest cover\data\basin_data\Tevere_ESA_2000.tif"
    glc_path = r"C:\Users\user\OneDrive - Politecnico di Milano\00GLANCE_Forest cover\data\basin_data\Tevere_GLC_2000.tif"

    # ----------------------------
    # Output folder
    # ----------------------------
    output_dir = r"C:\Users\user\OneDrive - Politecnico di Milano\PhD_Keerthana\subjects\Geospatial processing\project"
    output_subdir = os.path.join(output_dir, "output")  # subfolder inside your project folder
    os.makedirs(output_subdir, exist_ok=True)

    # ----------------------------
    # Output file paths
    # ----------------------------
    cm_csv = os.path.join(output_subdir, "tevere_cfm_2000.csv")
    acc_csv = os.path.join(output_subdir, "tevere_accuracy_summary_2000.csv")
    cm_png = os.path.join(output_subdir, "tevere_cfm_htmap_2000.png")

    # ----------------------------
    # Load raster data
    # ----------------------------
    print("Loading rasters...")
    cci = load_raster(cci_path)
    glc = load_raster(glc_path)

    cci_flat = cci.flatten()
    glc_flat = glc.flatten()

    # ----------------------------
    # Compute confusion matrix
    # ----------------------------
    print("Computing confusion matrix...")
    cm = compute_confusion_matrix(cci_flat, glc_flat)

    print("Saving confusion matrix to:", cm_csv)
    cm.to_csv(cm_csv)

    # ----------------------------
    # Accuracy metrics
    # ----------------------------
    oa = overall_accuracy(cm)
    kappa = kappa_coefficient(cm)
    pa = producers_accuracy(cm)
    ua = users_accuracy(cm)

    mean_pa = np.nanmean(pa)
    mean_ua = np.nanmean(ua)

    # ----------------------------
    # Save summary CSV
    # ----------------------------
    accuracy_summary = pd.DataFrame({
        "Metric": [
            "Overall Accuracy",
            "Kappa Coefficient",
            "Mean Producer's Accuracy",
            "Mean User's Accuracy"
        ],
        "Value": [
            oa,
            kappa,
            mean_pa,
            mean_ua
        ]
    })

    print("Saving accuracy summary to:", acc_csv)
    accuracy_summary.to_csv(acc_csv, index=False)

    # ----------------------------
    # Plot confusion matrix
    # ----------------------------
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")   
    plt.title("Confusion Matrix ESA CCI vs GLC (MOLCA classes)")
    plt.xlabel("Predicted (GLC)")
    plt.ylabel("True (ESA CCI)")
    plt.savefig(cm_png, dpi=300, bbox_inches="tight")
    plt.close()

    print("\n✅ All outputs saved successfully in:")
    print(output_subdir)
 