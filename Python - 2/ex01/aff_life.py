# %%
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life():
    data = load('life_expectancy_years.csv')
    if data is None:
        print("Loading Data Failed!")
        return

    countryData = data[data['country'] == 'Morocco']
    years = countryData.columns[1:]
    life_exp = countryData.iloc[0, 1:]
    x_ticks = years[0::40]

    try:
        plt.plot(years, life_exp)
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title("Morocco Life expectancy Projections")
        plt.xticks(x_ticks)
        plt.show()
    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        print(f"Error: {e}")
        return None


def main():
    aff_life()


if __name__ == "__main__":
    main()
# %%
