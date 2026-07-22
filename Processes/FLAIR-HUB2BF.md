# Process : FLAIR-HUB2BF

* This is the description of the process FLAIR-HUB2BF which consists in generating building footprints for
the IasiStudy (https://github.com/subdense/dashboard/blob/master/Studies/IasiStudy.md) for the year 2024. This was needed because of the lack of the reliable building footprints in 2024. 
## InputData 1 : Orthophoto_year1
Orthophoto for the study area in year 2024 : RO-IAS-Orthophoto-2024.

## OutputData 1 : RO-IAS-Building-2021 (and its metadata)
Dataset corresponding to building footprints for 2024, structured as a geopackage containing the dataset. (GeoPackage `.gpkg`: A more modern format offering better performance and greater flexibility)
A description of this dataset within [Subdense “IasiStudy”](https://github.com/subdense/dashboard/blob/master/Studies/IasiStudy.md) registry.

## Tools used : 
* Model FLAIR-HUB
* Python
* QGIS

## Method overview
 ii) ; iii) . This is achieved by a home-made python algorithm
## Step 1 : Apply FLAIR-HUB model to infer LC classes
* to apply FLAIR-HUB model for windows in order to infer LC classes, please follows the [Manual](https://github.com/subdense/dashboard/blob/master/Processes/INSTALL-FLAIR-HUB-MODEL.pdf)
* The output of the model is raster image, where each pixel is classified with respect to the [nomenclature](https://www.sciencedirect.com/science/article/pii/S0924271626001899).
## Step 2 : Binarization 
* Consists in binarization of the resulting LC classification to obtain a binary mask containing only building pixels (LC class equals 0).
* The process is described here. [ComputeBuildingBinzarization.md](https://github.com/subdense/dashboard/blob/master/Processes/ComputeBuildingBinzarization.md)
## Step 3 : Segmentation
* Consistis in applying a segmentation algorithm in order to segment the binary which enables the delineation of building footprints in vector format (polygons).
* The process is described here. [ComputeBuildingSegmentation.md](https://github.com/subdense/dashboard/blob/master/Processes/ComputeBuildingSegmentation.md)
## Step 4 : Generalization
* This step is a post-processing which is applied to remove noise and generalize building by using Douglas-Peucker.
* The process is described here. [GeneralizationBuildingFootprins.md ](https://github.com/subdense/dashboard/blob/master/Processes/GeneralizationBuildingFootprins.md)
## Step 5 : Apply the data schema and naming conventions, then generate a GeoPackage 

