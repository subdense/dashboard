# Process: GeneralizationBuildingFootprins

* This process describes FLAIR-HUB2BF, which aims to remove noise and smooth the building footprints generated for the IasiStudy 
(https://github.com/subdense/dashboard/blob/master/Studies/IasiStudy.md) area in 2024. This post-processing  was necessary because the automatically extracted building footprints 
contained excessive geometric detail and irregular boundaries.

## InputData 1 : building  footprints for 2024
* vector polygon class building

## OutputData 1 : building  footprints for 2024
* vector polygon class building

## Tools used 
* link to the algorithm https://github.com/subdense/dashboard/blob/master/Processes/Generalization_Building_Footprins.py

## Method

##Step 1 : filtering
* Filter building having less than 10m2
* The filter is applied in QGIS by using the area attribute 
##Step 2 : Generalisation
* Apply Douglas-Peucker with the following parameters
* The parameter provided to the algorithm is the Tolerance, expressed in the units of the coordinate system - in this case, meters
* For a tolerance of 0.8 m ≈ 4 pixels at 20 cm or 9.5 pixels at 8.4 cm, depending on the raster resolution
