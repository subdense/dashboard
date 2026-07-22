# Process: GeneralizationBuildingFootprins

* This process describes FLAIR-HUB2BF, which aims to remove noise and smooth the building footprints generated for the IasiStudy 
(https://github.com/subdense/dashboard/blob/master/Studies/IasiStudy.md) area in 2024. This post-processing  was necessary because the automatically extracted building footprints 
contained excessive geometric detail and irregular boundaries.

## InputData 1 : building  footprints for 2024

## OutputData 1 : building  footprints for 2024 

## Tools used 
* link to the algorithm to be added

## Method

##Step 1 : filtering
* Filter building having less than 10m2
* The filter is applied in QGIS by using the area attribute 
## Step 2 : Generalisation
* Apply Douglas-Peucker with the following parameters : 
