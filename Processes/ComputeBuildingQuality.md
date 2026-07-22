# Process : ComputeBuildingQuality  

## InputData 1 : BuildingDataSet_ForEvaluation
BuildingDataSet at a given time (see Process BuildingDataPreparation) that we want to assess its quality 
## InputData 2 : BuildingDataSet_GT
BuildingDataSet at the given time (see Process BuildingDataPreparation) that is used as ground truth to compare with BuildingDataSet_ForEvaluation

## OutputData 1 : BuildingChangeDataSet  (and its metadata)
Dataset corresponding to changes detected in buildings data and further refined, structured after the BuildingChangeSchema depicted in this folder, with the correct file naming, that is prepared as a shapefile, and as a geopackage containing the dataset plus a dedicated stylesheet (BuildingEvolution_style.qml) and ready to display. (Shapefile `.shp`: A widely used and recognized format in GIS. GeoPackage `.gpkg`: A more modern format offering better performance and greater flexibility)
A description of this dataset within Subdense “Dataset” registry.
This dataset is useful to identify commission and commission.

## OutputData 2 : MatchingLinksSet (and its metadata) 
MatchingLinks between homologous features from the BuildingDataSet_ForEvaluation and BuildingDataSet_GT datasets. 

## Method overview

Produce "raw" BuildingChange data based on two BuildingDataSet at the same time t1 (Step 1 below) 
The matching links are interpreted as follows:
* 1:1: A building existing in the real world is represented in both the GT dataset and the dataset under evaluation. Position and shape accuracies can be computed.
* 1:0: A building is present in the BuildingDataSet_ForEvaluation  dataset but missing from the BuildingDataSet_GT dataset, corresponding to a commission error.
* 0:1: A building is present in the BuildingDataSet_GT dataset but absent from the BuildingDataSet_ForEvaluation dataset, corresponding to an omission error.
m:n: Multiple geometries are linked and require further inspection. For example, two attached buildings in the real world may be detected as a single building footprint by the FLAIR-HUB2BF process, while the GT dataset represents them as two separate building footprints.     

## Step 1 : Produce "raw" BuildingChange from Building Data

This first step is fully automatic. It uses matching libraries to produce matching links and automatically derive BuildingChanges from these links.

1. **Clone the Subdense Matching Repository**:
   - If not installed yet install GitHub Desktop available at [GitHub Desktop's official website](https://desktop.github.com/).
   - Visit the [Subdense Matching repository on GitHub](https://github.com/subdense/matching).
   - Use GitHub Desktop to clone it to a local directory.
  
2. **Add Input Data**: 
   - Place input data in `/data/bati`, with two layers representing building data at the same time T1.

3. **Install Python 3**:
   - Ensure Python 3 is installed on your system. Download from [Python's official website](https://www.python.org/downloads/).
   - Install jpype1, shapely, numpy,networkx, tqdm, pyogrio and geopandas using `pip3 install [module_name]`.
   - Use `pip3` if multiple Python versions are installed; consider proxy settings if applicable.
   - 
4. **Option1 : use Visual Studio** :
 - Install Visual Studio Code from [Visual Studio Code's website](https://code.visualstudio.com/).
 - Open Local Repository in Visual Studio Code:
   - Navigate to the local `matching` repository.
   - Right-click and select "Open with Visual Studio Code".
   - Open `run.py` in Visual Studio Code.
   - This script automates the execution of `matching.py` and applies the necessary data processing.
   - Modify the script if needed to align with your data paths and settings.

   **Option2 : use command line** : 
   For users comfortable with the command line, the script can also be executed via a terminal using the following command:
```bash
python run.py -layer1 ./data/ro/iasi_building_2024.gpkg -layer2 ./data/ro/iasi_building_2024_gt.gpkg -attributes '["HAUTEUR","ID"]' -output_prefix RO_IASI -java_memory 16G
```
This command runs `run.py` with specific parameters:
- `-layer1` and `-layer2` specify the paths to the building data for the years 2011 and 2021, respectively.
- `-attributes` allows the inclusion of specific attributes in the analysis, such as 'HAUTEUR' and 'ID'.
- `-output_prefix` sets the prefix for the output files, in this case 'RO_IASI' for Iasi, Romania.
- `-java_memory` allocates Java memory for the process, set here to 16 Gigabytes.
Ensure that the paths and parameters are adjusted as per your specific data and system requirements.

At the end of step 4, after running the code, two new files are generated in the `output_data` folder: `xxx_CHANGE` and `xxx_Matching_Links` in chosen formats.

Prepare an entry in the Dataset.md registry to register these data -at least the Evolution dataset- and put the minimal info. 

5. **Apply Stylesheet**:
   - Open xxx_CHANGE in QGIS for analysis and visualization, apply the `BuildingChangeStyle` file from the "ComputeBuildingChange" folder for optimal display.






