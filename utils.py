import os
import tarfile
import zipfile
import csv
from collections import OrderedDict

import pandas as pd

csv_list = ["TMDB_distribution.csv", "TMDB_info.csv", "TMDB_overview.csv"]

# Aquí comencen les funcions creades per l'exercici 1
def extract_tar(file: str, folder_destination: str) -> bool:
    """
    Descomprimir arxiu tar.gz
    :param file: Zip a descomprimir
    :param folder_destination: Carpeta de destí
    :return: bool de si l'ha descomprimit
    """
    try:
        with tarfile.open(file) as tar:
            print("Extracting tar.gz")
            tar.extractall(folder_destination)
        return True
    except Exception as error:
        print(error)
        return False


def unzip(file: str, folder_destination: str) -> bool:
    """
    Descomprimir arxiu zip
    :param file: Zip a descomprimir
    :param folder_destination: Carpeta de destí
    :return: bool de si l'ha descomprimit
    """
    try:
        with zipfile.ZipFile(file, 'r') as zip:
            print("Extracting zip")
            zip.extractall(folder_destination)
        return True
    except Exception as error:
        print(error)
        return False


def decompress_file(file: str) -> str:
    """
    Descomprimeix un arxiu zip o tar.gz
    :param file: Arxiu a descomprimir
    :param folder_destination: Carpeta de destí. Per defecte és la carpeta actual
    :return: Carpeta de destí on s'ha 
    """
    global folder_decompress
    if not os.path.isfile(file):
        file = input("Si us plau, insereix la ruta de l'arxiu zip a descomprimir (ex: ./data/arxiuZip.zip): ")
        if not os.path.isfile(file):
            print(f"Ho sentim, però {file} no és un arxiu vàlid.")
            exit()
            return False
    extension = os.path.splitext(file)[1]
    folder_decompress = os.path.dirname(file)
    if extension == '.zip':
        return unzip(file, folder_decompress)
    if extension == '.tar.gz':
        return extract_tar(file, folder_decompress)
    print("This file can't be extracted as it's not .zip or .tar.gz")


def check_number_elements(lst: list, num: int) -> bool:
    """
    Comprovar que una llista té el número d'elements necessaris
    :param lst: La llista a què comprovar els elements
    :param num: Número d'elements que volem que tingui la llista
    :return:
    """
    if len(lst) == num:
        return True

    print(f"{num} elements are needed.")
    return False


def merge_csv_with_pd(csvs: list, key: str) -> pd.DataFrame:
    """
    Llegeix els 3 csvs i els passa a un dataframe conjunt
    :param csvs: Llista dels csv a processar
    :param key: Nom del camp clau a l'hora d'unir els csvs
    :return: DataFrame unificat amb tots els valors
    """
    global folder_decompress
    if not check_number_elements(csvs, 3):
        return None

    print("Creating dataframes")
    df1 = pd.read_csv(os.path.join(folder_decompress, csvs[0]))
    df2 = pd.read_csv(os.path.join(folder_decompress, csvs[1]))
    df3 = pd.read_csv(os.path.join(folder_decompress, csvs[2]))

    print("Merging dataframes")
    df_final = df1.merge(df2, how="outer", on=[key])
    df_final = df_final.merge(df3, how="outer", on=[key])
    return df_final


def read_csv_with_csv(csvs: list, key: str) -> dict:
    """
    Funció per ajuntar 3 csv en un retornant-ho en forma de diccionar
    :param csvs: Llista dels csv a processar
    :param key: Nom del camp clau a l'hora d'unir els csvs
    :return: Un diccionari unificat amb tots els valors
    """
    global folder_decompress
    if not check_number_elements(csvs, 3):
        return None
    dict_values = {}
    # Es podria mirar de posar tot en un diccionari amb la clau del id
    print("Creating dictionary from csv files")
    for c in csvs:
        path_csv = os.path.join(folder_decompress, c)
        with open(path_csv, 'r') as doc:
            dict_csv = csv.DictReader(doc)
            for row in dict_csv:
                if dict_values.get(row[key]) == None:
                    dict_values[row[key]] = {}
                for col in row.keys():
                    if col != key:
                        dict_values[row[key]][col] = row[col]
    return dict_values


# Aquí comencen les funcions creades per l'exercici 2
def check_variable_assigned(variable_name: str) -> bool:
    """
    Funció per a comprovar si una variable ja està assignada
    :param variable_name: Nom de la variable a comprovar
    :return: Un booleà de si ha estat assignada la variable o no
    """
    return variable_name in globals()


def get_df():
    """
    Funció que descomprimeix el zip en cas de ser necessari i que ajunta els csv en un de sol
    :return: Un DataFrame amb els 3 csv junts
    """
    global csv_list
    for csv_file in csv_list:
        if not os.path.isfile(csv_file):
            decompress_file('./data/TMDB.zip')
            break
    return merge_csv_with_pd(csv_list, "id")


def get_day_difference_pd(df: pd.DataFrame, col1: str, col2: str, date_format: str = "%Y-%m-%d") -> pd.Series:
    """
    Funció per a treure la diferència de dies entre dues columnes d'un dataframe
    :param df: Dataframe principal de què volem treure la diferència de dies
    :param col1: Nom de la columna amb la primera data
    :param col2: Nom de la columna amb la segona data
    :param date_format: Format de les dates. Per defecte és any-mes-dia.
    :return: Retorna un objecte Series amb els dies de diferència
    """
    date_format_1 = pd.to_datetime(df[col1], format=date_format)
    date_format_2 = pd.to_datetime(df[col2], format=date_format)
    return (date_format_2 - date_format_1).dt.days


def concat_two_columns(df: pd.DataFrame, col1: str, col2: str) -> pd.Series:
    """
    Funció per a concatenar dues columnes en una sola
    :param df: Dataframe inicial
    :param col1: Primera columna a concatenar
    :param col2: Segona columna a concatenar
    :return: Un objecte Series amb la concatenació de les dues columnes
    """
    return df[col1] + df[col2]


def get_ordered_dict_full_path(df: pd.DataFrame) -> OrderedDict:
    """
    Funció que crea un diccionari ordenat de les rutes dels posters
    :param df: Dataframe del qual crear el diccionari ordenat
    :return: Un OrderedDict amb el nom dels programes i les rutes senceres dels posters
    """
    df["full_poster_path"] = concat_two_columns(df, "homepage", "poster_path").fillna("NOT AVAILABLE")
    ordered_dict = OrderedDict()
    print("Loading ordered dictionary")
    for index, row in df[["name", "full_poster_path"]].iterrows():
        ordered_dict[row['name']] = row["full_poster_path"]
    return ordered_dict


def get_first_n_elements_from_dict(ordered_dict: OrderedDict, num: int)-> dict:
    """
    Funció per retornar els primers N elements d'un diccionari
    :param ordered_dict: Diccionari ordenat de què volem recuperar els elements
    :param num: Número d'elements que volem recuperar
    :return: Diccionari dels primers N elements"""
    return dict(list(ordered_dict.items())[:num])


# Aquí comencen les funcions creades per l'exercici 3
def get_mystery_crime_in_english(df: pd.DataFrame) -> list:
    """
    Funció per a recuperar aquells programes que estiguin en anglès i
    parlin de 'mystery' o 'crime' a la descripció
    :param df: Dataframe en què buscar els programes
    :return: Una llista amb tots els programes trobats
    """
    mystery_crime_en = df[(df.original_language == "en")
                    & (df.overview.str.contains("mystery", case=False) | df.overview.str.contains("crime", case=False))]
    list_mystery_crime_en = list(mystery_crime_en["name"])
    print(f"\nList of the {len(list_mystery_crime_en)} programs in english that includes 'mystery' or 'crime':")
    print(list_mystery_crime_en)
    return list_mystery_crime_en

def get_canceled_shows_by_start_year(df: pd.DataFrame, year: str) -> pd.DataFrame:
    """
    Funció per a recuperar aquells programes cancel·lats i que comencessin en un cert any
    :param df: Dataframe en què buscar els programes
    :param year: Any en què comencen els programes. S'haurà de posar com a string
    :return: Un Dataframe amb tots els programes trobats
    """
    canceled = df[(df.first_air_date.str.startswith(year, na=False)) & (df.status == "Canceled")][["name", "first_air_date", "status"]]
    print(f"\nList of 20 of the canceled shows started in {year}")
    print(canceled.head(20))
    return canceled

def get_language_shows(df: pd.DataFrame, language: str) -> pd.DataFrame:
    """
    Funció per a recuperar aquells programes que estiguin en cert idioma
    :param df: Dataframe en què buscar els programes
    :param language: Idioma en què volem trobar els programes
    :return: Un Dataframe amb tots els programes trobats
    """
    language_shows = df[(df.languages.str.contains(language, na=False))][["name", "original_name", "networks", "production_companies"]]
    pd.set_option('display.max_columns', None)
    print(language_shows.head(20))


# Aquí comencen les funcions creades per l'exercici 4
def get_years(df: pd.DataFrame, colname: str) -> pd.DataFrame:
    """
    Funció per a extreure els anys d'una columna de data de dataframe
    :param df: DataFrame en què hi ha la columna de data
    :param colname: Nom de la columna que conté el camp de la data
    :return: Un DataFrame amb la columna transformada a anys
    """
    years = df[colname].str.extract(r'([0-9]{4})').astype('Int64')
    return years

if __name__ == '__main__':
    df_pd = get_df()
    print(type(get_years(df_pd, "first_air_date")))



