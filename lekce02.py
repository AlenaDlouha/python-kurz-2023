#jmena = ["martin", "Michal", "Milada", "Jana"]

knihy = ["Temna noc", 450, True, True]
knihy[0] = "Milosrdna vrazda"

knihy2 = {
    "Nazev": "Ananas na pizzu patri",
    "Cena": 0,
    "Skladem": True
}

print(knihy2)
print(knihy2.keys())
print(knihy2.values())
print(knihy2["Nazev"])
print(f"Kniha: {knihy2['Nazev']}, Cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")

knihy2["Cena"] = 100

print(f"Kniha: {knihy2['Nazev']}, Cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")

k