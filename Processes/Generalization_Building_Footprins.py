# Generalization_Building_Footprins.py
# The Douglas–Peucker algorithm is used to simplify a geometry by removing vertices that contribute little information to the overall shape
# The parameter provided to the algorithm is the Tolerance, expressed in the units of the coordinate system - in this case, meters

import os
import geopandas as gpd

# -----------------------------
# PARAMÈTRES
# -----------------------------

INPUT_DIR = r"D:\(The path to the folder)"
OUTPUT_DIR = r"D:\(The path to the folder)"

TOLERANCE = 0.8  # meters (For a tolerance of 0.8 m ≈ 4 pixels at 20 cm or 9.5 pixels at 8.4 cm, depending on the raster resolution)
                 # meters (For a tolerance of 0.4 m ≈ 2 pixels at 20 cm or 4.8 pixels at 8.4 cm, depending on the raster resolution)

os.makedirs(OUTPUT_DIR, exist_ok=True)

print(" Input file :", INPUT_DIR)
print(" Output file :", OUTPUT_DIR)
print(" Tolerance DP :", TOLERANCE, "m")

# -----------------------------
# TRAITEMENT
# -----------------------------

processed = 0

for file in os.listdir(INPUT_DIR):

    if not file.lower().endswith(".shp"):
        continue

    in_path = os.path.join(INPUT_DIR, file)

    # Output name with _DP suffix
    base, ext = os.path.splitext(file)
    out_file = base + "_DP" + ext
    out_path = os.path.join(OUTPUT_DIR, out_file)

    print(f"▶ Simplification : {file}")

    gdf = gpd.read_file(in_path)

    if gdf.empty:
        print("Empty shapefile → ignored")
        continue

    # Safety: valid geometries
    gdf = gdf[gdf.geometry.notnull()].copy()

    # Douglas–Peucker
    gdf["geometry"] = gdf.geometry.simplify(
        tolerance=TOLERANCE,
        preserve_topology=True
    )

    gdf.to_file(out_path)

    print(f"  ✔ Saved : {out_file}")
    processed += 1

print(f"\n✅ Douglas–Peucker simplification complete ({processed} fichiers)")

