import geopandas as gpd

# Chemin des fichiers. Tbd : change this so that it is not hard-coded and that no output but modification of input
input_file = 'set your path to xxx-CHANGE.gpkg'
output_file = 'set your path to xxxx-2011-21.gpkg'
readme_file = 'set your path to xxx-CHANGE-Log.md'

# Charger la couche d'évolution du bâti
gdf = gpd.read_file(input_file)

# Calculer la superficie en mètres carrés pour tous les bâtiments
gdf['area_m2'] = gdf.geometry.area

# Supprimer les attributs 'HAUTEUR_1', 'HAUTEUR_2' et 'area_ha'
gdf = gdf.drop(columns=['HAUTEUR_1', 'HAUTEUR_2', 'area_ha'])

# Renommer les attributs 'ID_1' et 'ID_2'
gdf = gdf.rename(columns={'ID_1': 'ID_Building_2011', 'ID_2': 'ID_Building_2021'})

# Initialiser les nouveaux champs avec les valeurs par défaut
gdf['changeProduct'] = 'No'
gdf['qualityControl'] = 'Undefined'
gdf['changeEntities'] = 'No'

# Détecter et traiter les bâtiments apparus de superficie < 50 m2
appeared_below_50m2 = gdf[(gdf['type'] == 'appeared') & (gdf['area_m2'] < 50)]
nb_appeared_below_50m2 = len(appeared_below_50m2)
gdf.loc[(gdf['type'] == 'appeared') & (gdf['area_m2'] < 50), ['type', 'changeProduct', 'changeEntities']] = ['stable', 'Yes', 'No']
appeared_below_50m2_ids = appeared_below_50m2['id'].tolist()

# Détecter et traiter les bâtiments de type split
split_buildings = gdf[gdf['type'] == 'split']
nb_split_buildings = len(split_buildings)
gdf.loc[gdf['type'] == 'split', ['type', 'changeProduct', 'changeEntities']] = ['stable', 'Yes', 'No']
split_buildings_ids = split_buildings['id'].tolist()

# Générer le fichier README
with open(readme_file, 'w') as file:
    file.write("# FR-STR-FUA-Evolution-201121-RefineEvolutionBDTopoLog\n")
    file.write("\n")
    file.write("## Detection des changements de type appeared de batiment inferieurs a 50m2\n")
    file.write(f"Nombre de changements détectés : {nb_appeared_below_50m2}\n")
    file.write("\n")
    file.write("## Changement du type d’appeared a stable, de changeProduct a YES, de changeEntities a NO pour toutes ces évolutions\n")
    file.write(f"Liste des identifiants : {appeared_below_50m2_ids}\n")
    file.write("\n")
    file.write("## Detection des évolutions de type split de batiment\n")
    file.write(f"Nombre d’évolutions détectées : {nb_split_buildings}\n")
    file.write("\n")
    file.write("## Changement du type de split a stable, de changeProduct a YES, de changeEntities a NO pour toutes ces évolutions\n")
    file.write(f"Liste des identifiants : {split_buildings_ids}\n")

# Sauvegarder la nouvelle couche dans un fichier GeoPackage tbd : change so that the input file is changed.
gdf.to_file(output_file, layer='FR-STR-FUA-EVOLUTION-2011-21', driver='GPKG')
