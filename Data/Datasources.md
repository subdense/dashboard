# Datasources 

List of datasources mentioned, investigated, possibly used for the dashboard. The purpose of this registry is not to duplicate existing catalogues but rather to log and share feedback on their relevance and usability in the dashboard context. A datasource can be : a product, a project, a web portal.  

*******
 1. [BDTOPO-FR](#bdtopo-fr)
 2. [EUBUCCO](#eubucco)
 3. [ATKIS-DE](#atkis-de)
 4. [GHSL UCDB](#ghsl-ucdb)
 5. [OPENZOOM-UK](#openzoom-uk)
 6. [OSM](#osm)
 7. [OSMASTERMAP-UK](#osmastermap-uk)
 8. [OSNGD-UK](#osngd-uk)
 9. [OCS-GE2-FR](#ocs-ge2-fr)
 10. [OpenDataStrasbourg-FR](#opendatastrasbourg-fr)
 11. [BasedeDonnéesNationaleIMOPE-InventaireMulti-ObjetsdesBâtiments](#base_de_donnees_nationale_imope_-_inventaire_multi-objets_des_batiments)
 12. [DonnéesSocioÉconomique-INSEE-FR](#donneessocioeconomique-insee-fr)
 13. [Géométries-des-IRIS-IGN-FR](#geometries-des-iris-ign-fr)
 14. [CadastralData-FR](#cadastraldata-fr)
 15. [FONCIER-CEREMA-FR](#foncier-cerema-fr)
 16. [SITADEL-DAU-DemandesAutorisationUrbanisme-FR](#SITADEL-DAU-DemandesAutorisationUrbanisme-FR)
*******

## BDTOPO-FR 
* **status related to dashboard process** : has been used on StrasbourgStudy, to be used for ToulouseStudy (late 2024)
* **Available Documentation** :
    * [Standard ISO19139 metadata](https://geoservices.ign.fr/sites/default/files/2023-01/IGNF_BDTOPOr_3-3.html)
    * Detailed documentation : [different documents describe the current product and past versions](https://geoservices.ign.fr/documentation/donnees/vecteur/bdtopo), a key document is [DC_BDTOPO_3-3](https://geoservices.ign.fr/sites/default/files/2024-05/DC_BDTOPO_3-3.pdf)
    * Quality control : the results of quality control are available per departement, like [for 67](https://geoservices.ign.fr/sites/default/files/2024-01/RCQ_BDTOPO_D67.pdf)
    * BD TOPO® | Géoservices (ign.fr), french, a fine description of content is available in french through an [interactive interface](https://geoservices.ign.fr/bd-topor-explorer-descriptif-de-contenu)
    * Additional metadata : there are additional metadata that are specific to communes or to departement and which are relevant to SUBDENSE, [their fine description](https://geoservices.ign.fr/sites/default/files/2023-01/DL_vecteur.pdf pp.14-16)
* **Clues to prepare BuildingDataSet on Temporal and Spatial scope of interest** :
    * Data can be downloaded either on whole France, or regions or departements. A download is associated to a set of metadata that is generic to BDTopo product.
    * On the city of Strasbourg, the BDTopo buildings 2022 vintage is using geometries from aerial imagery and no longer cadastral geometry so is more adapted to spatial analysis than the 2021 vintage which is using some geometries from cadastral (i.e. gutter and not wall). 
* **Quotes of Documentation RelevantToAStudy** :
    * the conceptual model for building in BDTopo is "Construction au-dessus du sol qui est utilisée pour abriter des humains, des animaux, des objets, pour la production de biens économiques ou pour la prestation de services et qui se réfère à toute structure construite ou érigée de façon permanente sur son site.", cf DC_BDTopo p54
* product versions : the current version of the product is 3.3. Shift from v2 to v3 took place between 2018 and 2019.
* stable identifier : see https://geoservices.ign.fr/sites/default/filhttps://geoservices.ign.fr/contoursirises/2023-01/IGNF_BDTOPOr_3-3.html "Depuis la version 3.0, tous les objets possèdent un identifiant unique et stable dans le temps." 
* change in selection criteria to represent buildings in the data : "Initialement, les seuils de sélection des bâtiments étaient les suivants : Tous les bâtiments de plus de 50 m² sont inclus. Les bâtiments faisant entre 20 et 50 m² sont sélectionnés en fonction de leur environnement et de leur aspect. Les bâtiments de moins de 20 m² sont représentés par un objet de classe Construction ponctuelle s’ils sont très
hauts, ou s’ils sont spécifiquement désignés sur la carte au 1 : 25 000 en cours (ex: antenne, transformateur…). Après unification de la BD TOPO® avec la BD PARCELLAIRE®, Tous les bâtiments présents dans la dernière édition de la BD PARCELLAIRE® vecteur sont inclus, sauf éventuellement des bâtiments manifestement détruits depuis la date de validité de la BD PARCELLAIRE®. Les petits bâtiments de la BD PARCELLAIRE® qui représentent des constructions ponctuelles (exemple des transformateurs) ou des constructions linéaires (exemple des murs de remparts) sont saisis avec leur modélisation initiale respective en BD TOPO®.
Il n’existe plus de seuil minimal pour la superficie des bâtiments. Cependant, si une nouvelle saisie photogrammétrique a lieu après les phases d’unification du bâti, les nouveaux bâtiments ne posséderont pas la granularité de la BD PARCELLAIRE®. Pour la restitution, les seuils de sélection initiaux sont alors appliqués (bâtiments de plus de 50 m² et bâtiments de 20 à 50 m² en fonction de leur environnement et de leur aspect)."
* change in building granularity : p55 "Les bâtiments BD PARCELLAIRE® ont une granularité plus fine que les bâtiments issus de BD TOPO® (découpage aux parcelles, aux extensions de bâtiment…). En conséquence, ce qui n’était qu’un bâtiment en BD TOPO® est représenté par plusieurs bâtiments après unification."
    

## EUBUCCO
* **status related to dashboard process** : has been identified, and documentation briefly reviewed, and feedback writen below
* **Documentation, short description** : https://docs.eubucco.com/  EUBUCCO is a scientific database of individual building footprints for 200+ million buildings across the 27 European Union countries and Switzerland, together with three main attributes – building type, height and construction year – included for respectively 45%, 74%, 24% of the buildings. EUBUCCO is composed of 50 open government datasets and OpenStreetMap that have been collected, harmonized and partly validated. 
* **Feedback** :  not available on the past decade. Yet, to follow up because the attributes are very relevant to the dashboard focus.

## ATKIS-DE
* **status related to dashboard process** : has been used on Dortmund, to be used for Frankfurt too (late 2024)
* **Documentation** for buildings on national level: https://gdz.bkg.bund.de/index.php/default/digitale-geodaten/sonstige-geodaten/amtliche-hausumringe-deutschland-hu-de.html

## GHSL-UCDB
* **status related to dashboard process** : ??
* * Global Human Settlement Layer Urban Center Database, https://ghsl.jrc.ec.europa.eu/
* **Documentation**  https://ghsl.jrc.ec.europa.eu/degurbaDefinitions.php
* {raw_data_link:"http://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_FUA_UCDB2015_GLOBE_R2019A/V1-0/GHS_FUA_UCDB2015_GLOBE_R2019A_54009_1K_V1_0.zip",
dataset_citation:"Schiavina M., Moreno-Monroy A., Maffenini L., Veneri P. (2019).: GHS-FUA R2019A - GHS functional urban areas, derived from GHS-UCDB R2019A, (2015), R2019A.European Commission, Joint Research Centre (JRC) 10.2905/347F0337-F2DA-4592-87B3-E25975EC2C95 PID:http://data.europa.eu/89h/347f0337-f2da-4592-87b3-e25975ec2c95",
paper_citation:"Moreno-Monroy A., Schiavina M., Veneri P. (2020). Metropolitan areas in the world. Delineation and population trends. Journal of Urban Economics. doi:10.1016/j.jue.2020.103242",
information:"https://ghsl.jrc.ec.europa.eu/ghs_fua.php"
}

## OPENZOOM-UK
* **status related to dashboard process** : has been identified when searching for documentation of OSMasterMap, not used yet
* **Documentation** : https://beta.ordnancesurvey.co.uk/products/os-open-zoomstack , english
* **Feedback** : Analysis and quotation of documentation relevant to SUBDENSE : 
https://www.ordnancesurvey.co.uk/documents/os-open-zoomstack-technical-specification.pdf?_gl=1*1jxmav3*_ga*NzE3NjU4MTY0LjE2ODEzNjk5Mjk.*_ga_59ZBN7DVBG*MTY4MTM2OTkyOS4xLjAuMTY4MTM2OTkyOS42MC4wLjA.&_ga=2.2835769.808952103.1681369930-717658164.1681369929 , p5 : “Generalised building footprints at both local and district resolutions. The local buildings have a unique identifier which can be used to style features distinctly.
The identifier will not be persistent between product versions and therefore there
will be no change history information for a feature.”

## OSM 
* **status related to dashboard process** : has been used in experiences to generate building evolution data but not adopted yet.
* **Feedback** : heterogeneity and lack of completeness in 2011 on some cities of interest

## OSMASTERMAP-UK
* **Documentation** : https://beta.ordnancesurvey.co.uk/products/os-mastermap-topography-layer 
* **Feedback** : Analysis and quotation of documentation relevant to SUBDENSE : 
Schema : geometries bear the themes. A building is a TopographicArea. 
“Attribute: TOID or gml:id
Definition: The unique topographic reference number. It consists of the letters ‘osgb’ followed by
thirteen or sixteen digits. The TOID must always be retained / stored in its entirety and any leading
zeros on the TOID are retained to permit linking of the feature to other OS MasterMap products”
“Attribute: changeHistory
Definition: Information about the change history of a feature that comprises the reason for the change and the date for this change. Each feature may have numerous change history records, and these are ordered chronologically. A complex attribute.”

## OSNGD-UK
* **Documentation** : https://www.ordnancesurvey.co.uk/business-government/new-data-access-methods?_gl=1*13idjk8*_ga*NzE3NjU4MTY0LjE2ODEzNjk5Mjk.*_ga_59ZBN7DVBG*MTY4MTM2OTkyOS4xLjEuMTY4MTM3MDIxNy41OS4wLjA.&_ga=2.81454110.808952103.1681369930-717658164.1681369929
* **Feedback** : this is an integration of OS data product into a unified product associated with user friendly web services to select relevant data.

## OCS-GE2-FR
* **Documentation** : https://ocs.geograndest.fr/compare   Access to a comparative tool between two available datasets (2007-2010 and 2010-2019)
An exploration of the data reveals that there have been no notable changes in the evolution of land use themes over the period studied. For example, if we look at changes in land use between 2010 and 2019, we only see an increase of 49 ha in built-up areas, but with a decrease in areas undergoing change and agricultural areas.
* **Feedback** : j'avais consulté cet outil pour voir si on peut observer une évolution de l'usage des sols, cette source peut être utile pour distinguer les zones constructibles ou potentiels de densifications.

  
## OpenDataStrasbourg-FR
* **status related to dashboard process** : To be used for StrasbourgStudy
* **Documentation** : https://data.strasbourg.eu/explore/?sort=modified  The open data provided by OpenDataStrasbourg provides several datasets valuable for our analysis :
    * A.  referentiel-topographique-simplifie : https://data.strasbourg.eu/explore/dataset/referentiel-topographique-simplifie/information/
        Ce jeu comporte plusieurs couches à savoir les adresses de début et de fin de tronçons, le bâti, le bâti public, les voies de communication, l’hydrographie et la toponymie. 
    * B.  referentiel_adresse_eurometrostras  : https://data.strasbourg.eu/explore/dataset/referentiel_adresse_eurometrostras/information/
    * C.  odata3d_lidar(Nuage de points 3D)   : https://data.strasbourg.eu/explore/dataset/odata3d_lidar/information/ 
        Nuage de points 3D haute densité obtenu par procédé Lidar aéroporté. On peut également faire des évolutions comparatives avce l'outil de visualisations sur         https://3d.strasbourg.eu/
* **Feedback** : le portail dispose plusieurs jeux de données, nous avons voulu remonter 10 ans en arrière mais nous ne pouvons pas télécharger les jeux de données par millésimes, nous avons  uniquement accès à la version la plus récente. Cette source est à suivre de près car elle présente une granularité plus fine dans le cadre l'étude sur Strasbourg.


## Base de Données Nationale IMOPE - Inventaire Multi-Objets des Bâtiments  
* **Documentation** : https://www.data.gouv.fr/fr/datasets/base-de-donnees-nationale-imope-inventaire-multi-objets-des-batiments
* **Feedback** :  Contacts pris, les coordinateurs ont indiqué qu’ils n’avaient pas encore de données sur 10 ans. D’après eux, la temporalité des données ne couvre que 3 années et seul le format déposé sur datagouv (couvrant l’année 2022) est actuellement disponible en open data. Toutefois le suivi de cette base de données est recommendé car elle présente des attributs pertinents

  
## DonnéesSocioÉconomique-INSEE-FR
* **status related to dashboard process** : On going on StrasbourgStudy
* **Documentation** : INSEE (National Institute of Statistics and Economic Studies) provides a wide range of socio-economic data for the French population, organized at different geographic levels (municipality, canton, department, and IRIS). The data cover various topics such as demographics, income, employment, education, and other socio-economic indicators. 
  * A. Série historique du recensement de la population : https://catalogue-donnees.insee.fr/fr/catalogue/recherche/DS_RP_SERIE_HISTORIQUE données historiques contenant les populations légales depuis 1968, des dénombrements sur les logements, des données d'état civil et de superficie. Période temporelle : 1968-2021
  * B. Recensement de la population à l’IRIS: https://www.insee.fr/fr/statistiques?debut=20&idprec=2028582&theme=1&categorie=1&geo=IRIS-1
  * C. base infracommunale « Logement »  : fournit des données sur des données sur les caractéristiques des résidences principales, la date d'emménagement, la possession d'une voiture ainsi que le parc de logements, maisons et appartements. temporalité : 2006-2020 https://www.insee.fr/fr/recherche/recherche-statistiques?q=iris&taille=50&debut=0&theme=7&categorie=5&geo=IRIS-1
* **Feedback** : utile sur le calcul des indicateurs; Sur l'étude de la densification, le croisement de ces données avec celles des bâtiments permet de calculer la corrélation entre l'évolution de la population par exemple et l'évolution des bâtiments. Des analyses comparatives peuvent êtres faites à l'echelle des iris, communes ou quartiers.

## Géométries-des-IRIS-IGN-FR
* **Documentation** : géométries des zones IRIS utilisées dans les données statistiques INSEE : https://geoservices.ign.fr/contoursiris
* **Feedback** : utile pour les intégrer dans le projet QGIS afin de réaliser des corrélations entre évolutions de batiments (agrégées a chaque IRIS) et données statistiques socioéconomiques.

## CadastralData-FR
* **Documentation** : https://cadastre.data.gouv.fr/datasets
* **Feedback** : Cadastral data is available with several editions ranging from 2017 to 2024 through the Computerized Cadastral Plan and cadastral data from the Eurometropolis of Strasbourg. The departmental files of computerized lineage documents (DFI) provide access to the history of cadastral parcels, including modifications since their digitization in the 1980s and 1990s. They detail the origin and dates of updates, derived from various documents such as surveys or reworkings. They track some of the parcel changes since 1990.

## FONCIER-CEREMA-FR
* **Documentation** : https://datafoncier.cerema.fr/obtention-des-donnees-foncieres
* **Feedback** : The property files come from the MAJIC application of the DGFIP and are supplemented by Cerema. They contain fiscal information primarily related to property tax, covering characteristics of the premises (such as the construction date and surface area), specifics of the parcels, as well as details about the owners, including their status (public or private) and addresses. This is an interesting source as it can be used for various purposes, particularly in observing territorial changes. These are annual data and can allow multi-period analyses ranging from broad dissemination to more detailed geolocation at the parcel level. The data is available and free for entitled parties. In accordance with the CNIL declaration signed by DGALN, they can provide us with previous editions within the limit of 10 years, from 2013 to 2022 (the oldest data dating back to 2009, we will not be able to go back 20 or 30 years).
* Access to this data is subject to an agreement with Cerema.

## SITADEL-DAU-DemandesAutorisationUrbanisme-FR
* **Acces aux données**: https://www.statistiques.developpement-durable.gouv.fr/catalogue?page=dataset&datasetId=6513f0189d7d312c80ec5b5b
* **Documentation** :  https://www.statistiques.developpement-durable.gouv.fr/catalogue?page=dataset&datasetId=6513f0189d7d312c80ec5b5b
* **Feedback** : Cette base permet de récupérer toutes les demandes de permis de construire et de travaux d'urbanisme depuis 2013, et leur suivi, en ne gardant que les travaux qui créent des logements. Les demandes sont localisées (voir méthode pour géoréférencer sur ce dashboard).    

