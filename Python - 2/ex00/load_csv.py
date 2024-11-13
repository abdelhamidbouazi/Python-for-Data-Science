import pandas as pd


def load(path: str):
    df = pd.read_csv(path)
    data = df.head(2)
    print(df)
    return None

def main():
    load("/Users/opus/Desktop/Python-for-Data-Science/life_expectancy_years.csv")

if __name__ == "__main__":
    main()