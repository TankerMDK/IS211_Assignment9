# scraped from https://en.wikipedia.org/wiki/List_of_Dragon_Ball_episodes

import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_episodes"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Gets all the tables.
tables = soup.find_all("table", class_="wikitable")

# Pulling Season 1
episode_table = tables[1]

episodes = []

rows = episode_table.find_all("tr")

real_episode_number = 1
for row in rows[1:]:
    columns = row.find_all("td")
    if len(columns) != 6:
        continue

    full_title = columns[0].text.strip()

    parts = full_title.split("Transliteration:")
    english_title = parts[0].strip().strip('"')
    japanese_title = parts[1].strip() if len(parts) > 1 else ""

    episodes.append({
        "episode": real_episode_number,
        "english_title": english_title,
        "japanese_title": japanese_title
    })

    real_episode_number += 1

# This code is working with the season 1 table at 13 episode.*
# Display sample in terminal
for ep in episodes[:13]:
    print(f"Episode {ep['episode']}: {ep['english_title']} / {ep['japanese_title']}")

# Save to JSON
with open("dragon_ball_episodes.json", "w", encoding="utf-8") as f:
    json.dump(episodes, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print("Running scrapper two...")
