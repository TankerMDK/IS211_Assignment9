# scraped from https://en.wikipedia.org/wiki/List_of_World_Series_champions

import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_World_Series_champions"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Need to find the rows first.
table = soup.find("table", class_="wikitable") #
rows = table.find_all("tr")

champions = []

for row in rows[1:]: # skips the header
    columns = row.find_all(["td", "th"])
    if len(columns) < 6:
        continue # to skip the notes

    year = columns[0].text.strip().split("[")[0]  # "[" Gets rid of the footnote
    winner = columns[1].text.strip().split("(")[0]
    series = columns[3].text.strip().split("[")[0]
    loser = columns[4].text.strip().split("(")[0]

    champions.append({
        "year": year,
        "winner": winner,
        "series_result": series,
        "loser": loser
    })
"""This is currently set to print 10 results"""
print(json.dumps(champions[:10], indent=2, ensure_ascii=False)) # ensure_ascii if fixing a unicode escape display issue.
                                                                # It works. But the json file editing needs work.

# Saving the json file
with open("world_series_champions.json", "w") as f:
    json.dump(champions, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print("Running scrapper one...")
