import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
    import numpy as np
except ImportError:
    raise ImportError(
        "pandas is not installed for the Python running these tests:\n"
        f"    {sys.executable}\n"
        "Select the Anaconda (conda) interpreter in VS Code: Ctrl/Cmd+Shift+P → "
        "'Python: Select Interpreter' → pick the one that says 'anaconda3'."
    ) from None

from src.fill_the_gaps import missing_year_games, fill_publishers, clean_years

DATA_PATH = REPO_ROOT / "data" / "vgsales.csv"

COLUMNS = ["Rank", "Name", "Platform", "Year", "Genre", "Publisher",
           "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

practice = pd.DataFrame([
    [1, "Alpha",   "A", 2001.0, "Action", "Nintendo", .5, .2, .1, .0, .8],
    [2, "Bravo",   "B", np.nan, "Sports", "Sega",     .3, .1, .0, .0, .4],
    [3, "Charlie", "A", 2003.0, "Racing", np.nan,     .2, .1, .0, .0, .3],
    [4, "Delta",   "C", np.nan, "Action", np.nan,     .1, .1, .0, .0, .2],
    [5, "Echo",    "B", 2005.0, "Puzzle", "Unknown",  .1, .0, .0, .0, .1],
], columns=COLUMNS)

RETURNED_NONE = "Function returned None. Did you replace `return None`?"
MISSING_YEAR = "Keep only rows where Year is blank, not rows with a blank in any column."
FILL_ONLY_PUBLISHER = "Fill only the Publisher column. Year should still have its blanks."
KEEP_ROWS = "Fill the blanks; don't drop any rows."
DROP_YEAR = "You dropped rows with any blank. Only games with a missing Year should go."


def run(function, df):
    """Call a student function. If it crashes, return the error as text so the test fails with a message."""
    try:
        return function(df)
    except Exception as error:
        return type(error).__name__ + ": " + str(error)


class VideoGameTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv(DATA_PATH)

    def check_table(self, result):
        if result is None:
            self.fail(RETURNED_NONE)
        if not isinstance(result, pd.DataFrame):
            self.fail("Should return a table (DataFrame). Got: " + repr(result)[:200])


class TestMissingYearGames(VideoGameTestCase):
    def test_real_data(self):
        result = run(missing_year_games, self.df.copy())
        self.check_table(result)
        self.assertEqual(len(result), 271, msg=MISSING_YEAR)
        self.assertTrue(result["Year"].isnull().all(), msg="Every Year in your table should be blank.")

    def test_practice_table(self):
        result = run(missing_year_games, practice.copy())
        self.check_table(result)
        self.assertEqual(list(result["Name"]), ["Bravo", "Delta"], msg=MISSING_YEAR)


class TestFillPublishers(VideoGameTestCase):
    def test_real_data(self):
        result = run(fill_publishers, self.df.copy())
        self.check_table(result)
        self.assertEqual(len(result), 16598, msg=KEEP_ROWS)
        self.assertEqual(result["Publisher"].isnull().sum(), 0, msg="Some Publishers are still blank.")
        self.assertEqual((result["Publisher"] == "Unknown").sum(), 261,
                         msg='Every blank Publisher should become "Unknown" (spelled exactly).')
        self.assertEqual(result["Year"].isnull().sum(), 271, msg=FILL_ONLY_PUBLISHER)

    def test_practice_table(self):
        result = run(fill_publishers, practice.copy())
        self.check_table(result)
        self.assertEqual(len(result), 5, msg=KEEP_ROWS)
        self.assertEqual(list(result["Publisher"]),
                         ["Nintendo", "Sega", "Unknown", "Unknown", "Unknown"],
                         msg='Every blank Publisher should become "Unknown" (spelled exactly).')
        self.assertEqual(result["Year"].isnull().sum(), 2, msg=FILL_ONLY_PUBLISHER)


class TestCleanYears(VideoGameTestCase):
    def test_real_data(self):
        result = run(clean_years, self.df.copy())
        self.check_table(result)
        self.assertEqual(len(result), 16327, msg=DROP_YEAR)
        self.assertEqual(result["Year"].isnull().sum(), 0, msg="Some Years are still blank.")

    def test_practice_table(self):
        result = run(clean_years, practice.copy())
        self.check_table(result)
        self.assertEqual(list(result["Name"]), ["Alpha", "Charlie", "Echo"], msg=DROP_YEAR)


if __name__ == "__main__":
    unittest.main()
