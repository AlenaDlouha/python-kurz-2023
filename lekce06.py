def vyuzij_dovolenou(zamestnanec, pocet_dni):
    if pocet_dni > zamestnanec["dovolena"]:
        print("Na toto nemas narok")
    else:
        print("Pozadavek schvalen")
        zamestnanec["dovolena"] = zamestnanec["dovolena"] - pocet_dni

zamestnanec4 = {
    "jmeno": "Alena Kucerova",
    "pozice": "IT Support",
    "dovolena": 25,
}

zamestnanec5 = {
    "jmeno": "Klara Kucerova",
    "pozice": "Senior IT Support",
    "dovolena": 25,
}


print(zamestnanec4["dovolena"])

class Zamestnanec:
    def __init__(self, jmeno, pozice, pocet_dni,plat, firma = "Czechitas"):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni = pocet_dni
        self.plat = plat
        self.firma = firma

    def vyuzij_dovolenou(self, dny):
        if dny > self.pocet_dni:
            return f"Na dovolenou mas narok, zbyva ti {self.pocet_dni}"
        else:
            self.pocet_dni = self.pocet_dni - dny
            return f"Na dovolenou mas narok, zbyva ti {self.pocet_dni}"



    def ziskej_informace(self):
        return f"Zamestnanec {self.jmeno}, pozice {self.pozice}, {self.pocet_dni}"    



Klara = Zamestnanec("Klara", "IT support", 25, 60000)
Matej = Zamestnanec("Matej", "Lektor", 20, 30000, "Gopas")



print(Klara.ziskej_informace())
print(Matej.ziskej_informace())

