import pandas as pd
import time
import lxml

print(lxml.__version__)


def get_draft_class(draft_year):
    url = f"https://www.basketball-reference.com/draft/NBA_{draft_year}.html"

    tables = pd.read_html(url)
    draft = tables[0]   # main draft table

    draft = draft[draft["Player"].notna()]

    draft["draft_year"] = draft_year
    draft["rookie_season"] = draft_year + 1

    return draft[["draft_year", "Player", "rookie_season"]]

seasons = list(range(2000, 2025))


dfs = []

for year in range(2000, 2025):
    try:
        df = get_draft_class(year)
        dfs.append(df)
        print(f"✓ {year}")
        time.sleep(2)
    except Exception as e:
        print(f"✗ {year}: {e}")

draft_classes = pd.concat(dfs, ignore_index=True)