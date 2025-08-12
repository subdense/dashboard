# Detect_DAU_Surelevation_BuildingChanges
## Input Sources
The core input for this analysis is the DAU dataset (Déclarations d’Autorisation d’Urbanisme), an administrative open dataset maintained by the French Ministry of Ecological Transition. It contains detailed records of urban development authorizations across France, including:

•	Location-based fields (e.g., street number, type, name, postal code).

• Time-related fields, such as the date of submission and the date of approval of the authorization.

•	Project type indicators, including “Indicateur de surélévation” for upward extensions.

•	Quantitative attributes, such as “Nombre de logements créés” (number of housing units created).

To validate and complement these administrative records, the project integrates aerial imagery (e.g., 2011, 2016, 2021 orthophotos) and multi-temporal MNS (Modèles Numériques de Surface) datasets. These spatial layers help visually verify construction changes and assess their vertical impact over time.

## Outputs
•	Output 1: A GIS-compatible dataset of upward extension projects in Strasbourg, with full addresses, construction dates, and number of new units.

•	Output 2: GIS-ready file — address points or simplified geometries that can be visualized and mapped in QGIS or similar tools for spatial analysis.

•	Output 3: A set of visually verified cases enriched by aerial/MNS imagery comparison.

## Method
The extraction and verification process of upward extensions (surélévations) involves the following steps:
1.	Filter DAU entries where Indicateur de surélévation = True;
2.	Construct a full address string by concatenating:
•	Numéro de voie du terrain + Type de voie du terrain + Libellé de la voie du terrain + Code postal du terrain + Localité du terrain + ", France";
•	Include the field “Nombre de logements créés” to capture the scale of densification.
3.	Export the filtered dataset in XLSX/CSV format for geocoding;
4.	Geocode addresses using QGIS (e.g., via MMQGIS plugin), producing a spatial point layer;
5.	Overlay multi-temporal aerial imagery (e.g., from 2011, 2014, 2016, 2018, 2021, etc.) to visually detect roof alterations or volumetric changes;
6.	Compare MNS (Modèle Numérique de Surface) layers from different periods to identify elevation gains:
•	Load MNS_année1.tif and MNS_année2.tif into QGIS;
•	Open Raster Calculator and enter the expression:
•	"MNS_année2@1" - "MNS_année1@1"
•	Export the resulting raster (e.g., Delta_MNS_diff.tif) to visualize height differences;
•	Positive ΔZ values suggest potential vertical additions.
7.	Extract ΔZ values at building locations:
•	Use zonal statistics or point sampling to retrieve elevation change at each geocoded DAU site;
•	Compare the measured ΔZ with the project metadata (authorization date, number of units, etc.).
8.	Select representative and verifiable cases:
•	Focus on sites where aerial imagery and MNS data clearly indicate upward extensions;
•	Include those with strong correlation between declared surélévation and observed elevation gain;
•	Prepare these for expert review and inclusion in the BuildingChanges Collection

