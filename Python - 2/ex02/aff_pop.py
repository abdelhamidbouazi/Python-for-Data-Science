# %%
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from matplotlib.ticker import FuncFormatter


def clean_pop(population):
    """
    function to clean the population and add a M (for millions) to it.
    """
    print(type(population))
    population = population.replace({'M': ''}, regex=True).astype(float)
    return population


def million_formatter(x, pos):
    """Formatter function to display values in millions"""
    return f'{int(x)}M'


def getData(data: pd.DataFrame, country: str):
    """returns the data of the given country
    Args:
        data (pd.DataFrame): DataFrame of the complete data
        country (str): The country wanted
    Returns:
        _type_: tuple of the country data
    """
    countryData = data[data['country'] == country]
    rows = countryData.columns[1:]

    years = [int(year) for year in rows]
    years = [year for year in years if year <= 2050]

    population = countryData.iloc[0, 1:len(years) + 1]
    population = clean_pop(population)
    return {"countryData": countryData, "years": years, "population": population}


def aff_pop():
    data = load('/goinfre/abouazi/Python-for-Data-Science/population_total.csv')
    if data is None:
        print("Loading Data Failed!")
        return

    morocco = getData(data, 'Morocco')
    france = getData(data, 'France')
    years = france['years']
    x_ticks = years[0::40]
    y_ticks = france['population'][0::20]

    try:
        fig, ax = plt.subplots()
        ax.plot(morocco['years'], morocco['population'], label='Morocco')
        ax.plot(france['years'], france['population'], label='France')
        ax.legend()
        ax.set_xlabel('Year')
        ax.set_ylabel('Population')
        ax.set_title('Population Projections')
        plt.xticks(x_ticks)
        ax.set_yticks([20, 40, 60])
        ax.yaxis.set_major_formatter(FuncFormatter(million_formatter))
        plt.show()
    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        print(f"Error: {e}")
        return None


def main():
    aff_pop()


if __name__ == "__main__":
    main()
# %%
