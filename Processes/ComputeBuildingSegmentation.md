# Process: ComputeBuildingSegmentation

* This is the description of the step 3 of process FLAIR-HUB2BF (https://github.com/subdense/dashboard/blob/master/Processes/FLAIR-HUB2BF.md) and consists in segmenting a binar raster image to extract building footprints. It is used in
the IasiStudy (https://github.com/subdense/dashboard/blob/master/Studies/IasiStudy.md) for the year 2024. This was needed because of the lack of the reliable building footprints in 2024. 

## InputData 1 : binar raster
* 1= building, 0= for everything that is not a building

## OutputData 1 : vector polygon layer 
* polygons

## Tools used 
* Polygon vectorization will be performed using the "Building_Segmentation.py" Python script within the FLAIR-HUB pipeline

## Method
** Link to the Method (https://github.com/subdense/dashboard/blob/master/Processes/Building_Segmentation.py)
