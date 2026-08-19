# Process: GeneralizationBuildingFootprins

* This process describes Step 4 of the FLAIR-HUB2BF process (https://github.com/subdense/dashboard/blob/master/Processes/FLAIR-HUB2BF.md), and aims to remove noise and smooth the building footprints generated for the IasiStudy 
(https://github.com/subdense/dashboard/blob/master/Studies/IasiStudy.md) area in 2024. This post-processing  was necessary because the automatically extracted building footprints 
contained excessive geometric detail and irregular boundaries.

## InputData 1 : building  footprints obtained for 2024 after a segmentation process (https://github.com/subdense/dashboard/blob/master/Processes/ComputeBuildingSegmentation.md)
* Vector layer containing building footprints as polygons

## OutputData 1 : building  footprints for 2024
* Vector layer containing building footprints as polygons
* RO-IAS-Building-2024 (without naming schema and its metadata).

## Tools used 
* Link to the algorithm https://github.com/subdense/dashboard/blob/master/Processes/Generalization_Building_Footprins.py

## Method

##Step 1 : Filtering
* Filter building having less than 10m2. This threshold has been applied in order to avoid noise (e.g. cars) or construction which are not dwelings. 
* The filter is applied in QGIS by using the area attribute

##Step 2 : Generalisation
* Apply Douglas-Peucker algorithm when Tolerance is a parameter to set
* The Tolerance needs to be expressed in the units of the coordinate system - in this case, meters
* Different values have been tested.
* The best results (visual validation) were obtained for the Tolerance equals to 0.8 m ( ≈ 4 pixels for the building footprints obtained from orthophotos with 20 cm resolution or ≈ 9.5 pixels for the building footprints obtained from orthophotos with 8.4 cm).
