from utils import *
import matplotlib.pyplot as plt


def labeling_plot(title: str, x_label: str, y_label: str):
    """
    Funció per a etiquetar una gràfica amb títol i els eixos.
    :param title: Títol de la gràfica
    :param x_label: Nom de l'eix X
    :param y_label: Nom de l'eix Y
    :return: None
    """
    plt.suptitle(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return None


def plot_hist_from_series(series: pd.Series, title: str, x_label: str, y_label: str, bins: int = 20):
    """
    Funció que fa un histograma a partir d'una Serie amb dades d'un cert camp
    :param series: Serie amb les dades de què es vulgui fer l'histograma
    :param title: Títol de la gràfica
    :param x_label: Nom de l'eix X
    :param y_label: Nom de l'eix Y
    :param bins: Quantitat de caixes que volem a l'histograma. Per defecte són 20.
    :return: None
    """
    series.plot.hist(bins=bins, legend=None)
    labeling_plot(title, x_label, y_label)
    plt.show()


def plot_bar_stacked(df_pd: pd.DataFrame, x_column_name: str, title: str, x_label: str, y_label: str):
    """
    Funció per fer una gràfica de barres apilades d'una columna d'acord amb la resta
    :param df_pd: DataFrame que conté la taula de freqüències amb la columna principal i la resta d'apilades
    :param x_column_name: Nom de la columna en què es basa l'eix X
    :param title: Títol de la gràfica
    :param x_label: Nom de l'eix X
    :param y_label: Nom de l'eix Y
    :return: None
    """
    df_pd.plot(x=x_column_name, kind="bar", stacked=True)
    labeling_plot(title, x_label, y_label)
    plt.show()
    return None


def plot_pie_chart(values: list, labels: list, title: str):
    """
    Funció per fer una gràfica circular dels valors insertats amb les etiquetes posades
    :param values: Llista de valors del camp que ens interessa
    :param labels: Nom de què pertany cadascun d'aquests valors
    :param title: Títol de la gràfica
    :return: None
    """
    if len(values) != len(labels):
        print("Les llistes insertades haurien de ser igual de grans")
        return None
    plt.pie(values, labels=labels, autopct="%1.1f%%", radius=1.2,
            pctdistance=0.9, colors=plt.cm.tab20.colors[:len(labels)])
    plt.suptitle(title)
    plt.show()
    return None

if __name__ == "__main__":
    df_pd = get_df()
    tabla = df_pd["genres"].str.split(', ').explode("genres").value_counts(normalize=True).mul(100)
    labels, main_genres_percentage = list(tabla[tabla >= 1].index), tabla[tabla >= 1].to_list()
    others = tabla[tabla < 1].to_list()
    labels.append("Other")
    main_genres_percentage.append(sum(others))
    print(sum(others))

    print(tabla)
    print(list(tabla.values))
    plt.pie(main_genres_percentage, labels=(labels), autopct="%1.1f%%", radius=1.2, pctdistance=0.9, colors=plt.cm.tab20.colors[:len(labels)])
    plt.show()
