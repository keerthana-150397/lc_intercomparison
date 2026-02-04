import os
import sys
import rasterio

def load_raster(path):
    """
    Loads a raster file and returns the first band as a NumPy array.
    """
    if not os.path.exists(path):
        print(f"❌ File does not exist: {path}")
        sys.exit(1)

    try:
        with rasterio.open(path) as src:
            arr = src.read(1)
            print(f"✅ Loaded raster: {path} | Shape: {arr.shape}")
            return arr
    except rasterio.errors.RasterioIOError as e:
        print(f"❌ Could not open raster: {path}\nError: {e}")
        sys.exit(1)