# Polygon vectorization will be performed using the "Building_Segmentation" Python script within the FLAIR-HUB pipeline
# Building_Segmentation.py  |It creates building polygons from a binary raster image in which the value 1 represents buildings and 0 represents the rest.

from pathlib import Path
import rasterio
from rasterio.features import shapes
import fiona
import numpy as np
import os

# --- Entry and exit ---
base_path = Path("D:/(The path to the folder)")

in_raster = base_path / "The binary file name.tif"
out_shp   = base_path / "The vector file name.shp"

# --- Debug ---
print("Raster path used :", in_raster)
print("Exists ?", in_raster.exists())

# --- Creation of the exit folder ---
os.makedirs(out_shp.parent, exist_ok=True)

# --- Raster reading ---
with rasterio.open(str(in_raster)) as src:
    image = src.read(1)
    mask = image > 0  # pixels non nuls
    
    # --- Polygonization or Segmentation ---
    results = (
        {'properties': {'value': int(v)}, 'geometry': s}
        for s, v in shapes(image, mask=mask, transform=src.transform)
    )
    
    # --- Creation of the shapefile ---
    schema = {'geometry': 'Polygon', 'properties': {'value': 'int'}}

    with fiona.open(
        str(out_shp), 'w',
        driver='ESRI Shapefile',
        crs=src.crs,
        schema=schema
    ) as shp:
        for elem in results:
            shp.write(elem)

print(f"✅ Polygonization complete : {out_shp}")