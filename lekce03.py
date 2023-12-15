import json

data = {
    "1. misto": "Olga",
    "2. misto": "Zanet",
    "3. misto": "Andy"
    }

with open("vyherci.json", mode="w", encoding="utf-8") as soubor:
    json.dump(data, soubor, ensure_ascii=False)

with open("vyherci.json", mode="r", encoding="utf-8") as soubor:
    vyherci = json.load(soubor)

print(vyherci)


import requests

url = requests.get("https://api.kodim.cz/python-data/people")
data = url.json()

for clovek in data:
    print(f"{clovek['first_name']} {clovek['last_name']}")

    import requests

url = requests.get("https://swapi.dev/api/people/1/")
data = url.json()
print(data)