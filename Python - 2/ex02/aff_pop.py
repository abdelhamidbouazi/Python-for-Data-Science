# %%
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def getData(data: pd.DataFrame, country: str):
    countryData = data[data['country'] == country]
    rows = int(countryData.columns[1:])

    years = rows[years <= 2050]
    population = countryData.iloc[0, 1:]
    print(f"[]")

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

    try:
        fig, ax = plt.subplots()
        ax.plot(france['years'], france['population'], label='Series 1')
        ax.plot(morocco['years'], morocco['population'], label='Series 1')
        
        ax.legend(title="Legend")
        
        
        ax.set_xlabel('year')
        ax.set_ylabel('population')
        ax.set_title('Overlay of Multiple Series')
        # plt.plot(france['years'], france['population'])
        # plt.plot(morocco['years'], morocco['population'])
        # plt.xlabel("Year")
        # plt.ylabel("Population")
        # plt.title("Morocco Life expectancy Projections")
        # plt.xticks(x_ticks)
        # plt.show()
    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        print(f"Error: {e}")
        return None


def main():
    aff_pop()


if __name__ == "__main__":
    main()
# %%
