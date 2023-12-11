import json

data = {
    "Dušan Kadlec": 32,
    "Daniel Svoboda": 100,
    "Anežka Benešová": 17,
    "Andrea Vaňková": 15,
    "Robin Blažek": 100,
    "Renáta Tichá": 81,
    "Matyáš Vaněk": 23,
    "Tereza Procházková": 3,
    "Luboš Černý": 64,
    "Vasyl Novotný": 66,
    "Jaroslav Polák": 7,
    "Dušan Kříž": 63,
    "Vlasta Kadlecová": 20,
    "Zdenka Soukupová": 100,
    "Igor Krejčí": 95,
    "Stanislav Vaněk": 90,
    "Julie Poláková": 40,
    "Veronika Fialová": 53,
    "Květoslava Dvořáková": 52,
    "Ladislav Čermák": 76,
    "Dana Marková": 98,
    "Miloš Horák": 78,
    "Štefan Jelínek": 37,
    "Miloš Veselý": 25,
    "Aleš Kříž": 22,
    "Marcela Machová": 11,
    "Blanka Kučerová": 67,
    "Šárka Marešová": 81,
    "Dalibor Kadlec": 8,
    "Robert Pospíšil": 36
}


# Vytvoření slovníku pro Pass/Fail hodnocení
prospech = {}
for jmeno, body in data.items():
    if body >= 60:
        prospech[jmeno] = "Pass"
    else:
        prospech[jmeno] = "Fail"

# Uložení do JSON souboru
with open("prospech.json", mode="w", encoding="utf-8") as soubor:
    json.dump(prospech, soubor)

with open("prospech.json", mode="r", encoding="utf-8") as soubor:
    prospech = json.load(soubor)

print(prospech)