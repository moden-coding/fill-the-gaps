# Exercise 30: Fill the Gaps

Clean up the missing values in a table of video game sales (`data/vgsales.csv`).

## Research questions

| # | Research question | Function | Returns | Look back at |
|---|---|---|---|---|
| 1 | Which games are missing a release year? | `missing_year_games(df)` | a table | Part 2 |
| 2 | Fill in every missing Publisher with `"Unknown"`. | `fill_publishers(df)` | a table | Part 2 |
| 3 | Keep only the games with a known release year. | `clean_years(df)` | a table | Part 2 |

## How to run

- See your findings: run `src/fill_the_gaps.py` (or `python src/fill_the_gaps.py` in the terminal).
- Run the tests from the Testing panel (beaker icon), or with `python -m unittest discover` in the terminal.

## If tests won't run

- Select the Anaconda (conda) interpreter: Ctrl/Cmd+Shift+P → "Python: Select Interpreter".
- If you have the old **Python Test Explorer** extension, uninstall it (`code --uninstall-extension littlefoxteam.vscode-python-test-adapter`). It ignores your interpreter.
- `pip install -r requirements.txt` if pandas is missing.
