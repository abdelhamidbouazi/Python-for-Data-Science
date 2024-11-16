# %%
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from matplotlib.ticker import FuncFormatter
import numpy as np


def extractData():
    """returns the data of the given country
    Args:
        data (pd.DataFrame): DataFrame of the complete data
        country (str): The country wanted
    Returns:
        _type_: tuple of the country data
    """
    income = load('/goinfre/abouazi/Python-for-Data-Science/income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_exp = load('/goinfre/abouazi/Python-for-Data-Science/life_expectancy_years.csv')
    if income is None or life_exp is None:
        print("Loading Data Failed!")
        return

    yearData_income = income['1900']
    yearData_lifeExp = life_exp['1900']

    return {"yearData_income": yearData_income.tolist(), "yearData_lifeExp": yearData_lifeExp.tolist()}


def projection_life():
    data = extractData()
    if data is None:
        return
    try:
        fig, ax = plt.subplots()
        x = data['yearData_income']
        y = data['yearData_lifeExp']
        np.corrcoef(x, y)
        plt.scatter(x, y)
        ax.set_ylabel('Life expectancy')
        ax.set_xlabel('Gross domestic product')
        ax.set_title('1900')
        plt.show()
    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        print(f"Error: {e}")
        return None


def main():
    projection_life()


if __name__ == "__main__":
    main()
# %%
