# %%
import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError) as e:
        print(f"Error: {e}")
        return None


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()

# %%
