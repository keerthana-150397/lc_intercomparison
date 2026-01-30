# Land-Cover Map Intercomparison (LC Intercomparison)

Project Overview

LC Intercomparison is a research-oriented Python framework developed as part of a PhD-level geospatial processing course. The project focuses on the pixel-wise intercomparison of land cover (LC) raster products and the quantitative evaluation of their agreement using standard accuracy assessment metrics widely adopted in remote sensing literature.

The framework is designed to support reproducible, transparent, and scientifically rigorous land-cover validation, with particular relevance to large-scale environmental and hydrological studies.

## Scientific Motivation
Land cover datasets derived from different sensors, classification algorithms, and temporal baselines often exhibit inconsistencies that can propagate uncertainty into downstream analyses (e.g., hydrological modeling, climate impact assessments, ecosystem monitoring).

This project aims to:
- Quantify agreement between two categorical land cover products
- Identify systematic classification differences
- Provide statistically sound accuracy metrics for comparative analysis

The methodology follows best practices recommended in the remote sensing accuracy assessment literature (e.g., confusion matrix–based evaluation).

## Methodology
The workflow implemented in this repository consists of the following steps:
1.  Raster ingestion
    Two categorical land cover GeoTIFF rasters (reference and comparison) are loaded using rasterio.
2.  Pixel-wise comparison
    Raster values are flattened and compared pixel by pixel to ensure a one-to-one correspondence.
3.  Confusion matrix computation
    A confusion matrix is generated, where rows represent reference classes and columns represent predicted classes.
4.  Accuracy metrics calculation
    The following metrics are derived:
      - Overall Accuracy (OA)
      - Cohen’s Kappa coefficient
      - Producer’s Accuracy (PA)
      - User’s Accuracy (UA)
5.  Output generation
    Results are exported as CSV tables and visualized using a confusion matrix heatmap.

## Repository Structure
lc_intercomparison/
├── lc_accuracy/                 # Core accuracy assessment modules
│   ├── lc_intercomparison_full.py
│   ├── utils.py
│   ├── test.py
│   └── __init__.py
├── output/                      # Generated outputs (CSV, figures)
│   ├── *_accuracy_summary_*.csv
│   ├── *_cfm_*.csv
│   └── *_cfm_htmap_*.png
├── .gitignore
├── LICENSE
├── README.md
└── github_installation.py


## Software Requirements
- Python ≥ 3.8
- Numpy
- Pandas
- Rasterio
- Matplotlib
- Seaborn

## Installation
Clone the repository:
git clone https://github.com/keerthana-150397/lc_intercomparison.git
cd lc_intercomparison

(Optional but recommended) Create a Conda environment:
conda create -n lc_intercomparison python=3.9 -y
conda activate lc_intercomparison

Install dependencies:
pip install numpy pandas rasterio matplotlib seaborn

## Usage
Edit the input paths in lc_intercomparison_full.py to point to your land cover raster datasets:
- Reference raster (e.g., ESA CCI)
- Comparison raster (e.g., GLC_FCS30)

Run the analysis:
python lc_accuracy/lc_intercomparison_full.py

All outputs will be saved automatically in the output/ directory.

## Outputs
The framework produces:
- Confusion matrix (CSV) – class-by-class comparison
- Accuracy summary (CSV) – OA, Kappa, mean PA, mean UA
- Confusion matrix heatmap (PNG) – visual representation of agreement
These outputs are suitable for inclusion in reports, course submissions, and scientific manuscripts.

## Data Assumptions & Notes
- Input rasters must have identical:
  - Projection
  - Spatial resolution
  - Extent
- No-data values should be handled prior to analysis
- Class harmonization (if needed) should be performed before running the script

## Academic Context
This project was developed as part of a PhD-level course in Geospatial Processing, with direct relevance to ongoing doctoral research on land cover change in Mediterranean basins.

