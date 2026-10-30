import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "vgsales.csv"


def missing_year_games(df):
    """Return a table of the games that are missing a release year."""
    return None


def fill_publishers(df):
    """Fill in every missing Publisher with "Unknown" and return the table."""
    return None


def clean_years(df):
    """Return a table of only the games with a known release year."""
    return None


def main():
    df = pd.read_csv(DATA_PATH)
    print("Games missing a release year:")
    print(missing_year_games(df))
    print()
    print("Missing publishers filled in:")
    print(fill_publishers(df.copy()))
    print()
    print("Games with a known release year:")
    print(clean_years(df))


if __name__ == "__main__":
    main()
