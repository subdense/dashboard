# Process: ComputeBuildingBinarization
* This is the description of the second step of the process [FLAIR-HUB2BF](https://github.com/subdense/dashboard/blob/master/Processes/FLAIR-HUB2BF.md) which consists in generating building footprints for the [IasiStudy.md](https://github.com/subdense/dashboard/blob/master/Studies/IasiStudy.md) for the year 2024. This was needed because of the lack of the reliable building footprints in 2024. 

## InputData 1 : Raster LandCover classification layer
* Raster LandCover classification, FLAIR-HUB pipeline output (15 classes)

## OutputData 1 : Raster binar class 
* 1= building, 0= for everything that is not a building

## Tools used 
* Binarization will be performed using the QGIS software's OSGeo4W Shell terminal

## Method
* Binarization is performed using the QGIS software's OSGeo4W Shell terminal
* Link to the method : https://github.com/subdense/dashboard/blob/master/Processes/Building_Binarization.txt
