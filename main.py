"""
Codi que executa tots els exercicis de la PAC 4
"""

import sys
import time
from utils import *
from plots import *

df_pd = pd.DataFrame()
folder_decompress = "."
csv_list = ["TMDB_distribution.csv", "TMDB_info.csv", "TMDB_overview.csv"]


def execute_all():
    """
    Funció per a executar tots els exercicis
    :return: None
    """
    execute_exercise_1()
    execute_exercise_2()
    execute_exercise_3()
    execute_exercise_4()
    execute_exercise_5()
    return None

def execute_exercise_1():
    """
    Executa el primer exercici de la PAC4
    :return: None
    """
    global df_pd, folder_decompress, csv_list
    print("\nExecuting 1.1")
    decompress_file('./data/TMDB.zip')

    print("\nExecuting 1.2")
    csv_list = ["TMDB_distribution.csv", "TMDB_info.csv", "TMDB_overview.csv"]
    start_time = time.time()
    df_pd = merge_csv_with_pd(csv_list, "id")
    end_time = time.time()
    time_1_2 = round(end_time-start_time, 2)
    print(f"Time required for exercise 1.2: {time_1_2} seconds")

    print("\nExecuting 1.3")
    start_time = time.time()
    df_dict = read_csv_with_csv(csv_list, "id")
    end_time = time.time()
    time_1_3 = round(end_time-start_time, 2)
    print(f"Time required for exercise 1.3: {time_1_3} seconds")

    print("\nExercici 1.4")
    if time_1_2*2 < time_1_3:
        doble = "més del doble"
    else:
        doble = "aproximadament el doble"
    print(f"""Podem veure que en el segon cas ens tarda {doble} del que ens ha tardat el primer.
D'aquí podem deduir que en cas de tenir un fitxer molt gran ens tardaria més amb aquesta segona funció. 
""")
    return True


def execute_exercise_2():
    """
    Executa el segon exercici de la PAC4
    :return: None
    """
    global df_pd, folder_decompress, csv_list
    if len(df_pd) == 0:
        df_pd = get_df()

    print("\nExercici 2.1")
    print("Creating new column named 'air_days'")
    df_pd["air_days"] = get_day_difference_pd(df_pd, "first_air_date", "last_air_date")
    print("Top 10 most aired programs")
    print(df_pd[["name", "air_days"]].sort_values('air_days', ascending=False).head(10))

    print("\nExercici 2.2")
    ordered_paths = get_ordered_dict_full_path(df_pd)
    print("First 5 elements from the ordered dictionary")
    print(get_first_n_elements_from_dict(ordered_paths, 5))

    return None


def execute_exercise_3():
    """
    Executa el tercer exercici de la PAC4
    :return: None
    """
    global df_pd, folder_decompress, csv_list
    if len(df_pd) == 0:
        df_pd = get_df()

    print("\nExercici 3.1")
    get_mystery_crime_in_english(df_pd)

    print("\nExercici 3.2")
    get_canceled_shows_by_start_year(df_pd, "2023")

    print("\nExercici 3.3")
    get_language_shows(df_pd, "ja")

    return None


def execute_exercise_4() -> None:
    """
    Executa el quart exercici de la PAC4
    :return: None
    """
    global df_pd, folder_decompress, csv_list
    if len(df_pd) == 0:
        df_pd = get_df()

    print("\nPlotting 4.1")
    print("Getting shows by starting year")
    df_pd["first_air_year"] = get_years(df_pd, "first_air_date").astype("Int64")
    print(df_pd["first_air_year"].value_counts())
    plot_hist_from_series(df_pd["first_air_year"], "Nombre de sèries per any d'inici", "Anys", "Número de programes", 50)

    print("\nPlotting 4.2")
    print("Getting show decades by type")
    df_pd["first_air_decade"] = (df_pd["first_air_year"] // 10) * 10
    decades_by_type = pd.crosstab(df_pd['first_air_decade'], df_pd['type']).reset_index().query('first_air_decade >= 1940')
    print(decades_by_type)
    plot_bar_stacked(decades_by_type, "first_air_decade", "Tipus de programa agrupats per dècades", "Dècades", "Número de programes")

    print("\nPlotting 4.3")
    print("Getting list of genres frequency")
    genres = df_pd["genres"].str.split(', ').explode("genres").value_counts(normalize=True).mul(100)
    print(genres)
    labels, main_genres_percentage = list(genres[genres >= 1].index), genres[genres >= 1].to_list()
    others = genres[genres < 1].to_list()
    labels.append("Other")
    main_genres_percentage.append(sum(others))
    plot_pie_chart(main_genres_percentage, labels, "Percentatge de programes segons gènere")

    return None


def execute_exercise_5():
    """
    Executa el quart exercici de la PAC4
    :return: None
    """
    #TODO
    return None

def main():
    """
    Funció principal per executar els exercicis
    :return: None
    """
    if len(sys.argv) == 1:
        execute_all()
        return None
    exercises_dict = {
        "1": execute_exercise_1,
        "2": execute_exercise_2,
        "3": execute_exercise_3,
        "4": execute_exercise_4,
        "5": execute_exercise_5
    }
    for arg in sys.argv[1:]:
        if arg in exercises_dict.keys():
            
            exercises_dict[arg]()
        else:
            print(f"L'exercici {arg} no existeix")
    return None
if __name__ == "__main__":
    main()
