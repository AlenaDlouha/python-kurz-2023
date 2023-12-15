class Zamestnanec:
    def __init__(self, jmeno, pozice, pocet_dni, plat, firma = "Czechitas"):
        self.prac_pozice = pozice
        self.jmeno = jmeno
        self.pocet_dni = pocet_dni
        self.plat = plat
        self.firma = firma

    def vyuzij_dovolenou(self, dny):
        if dny > self.pocet_dni:
            return f"Na toto nemas narok, zbyva ti {self.pocet_dni} dni"
        else:
            self.pocet_dni = self.pocet_dni - dny
            return f"Na dovolenou mas narok, zbyva ti {self.pocet_dni}"

 



    def __str__(self):
        return f"Zamestnanec {self.jmeno}, pozice {self.prac_pozice}, dovolena: {self.pocet_dni}, firma: {self.firma}"




class Manager(Zamestnanec):
    def __init__(self, jmeno, pozice, pocet_dni, pocet_podr, plat, firma = "Czechitas"):
        super().__innit__(jmeno, pozice, pocet_dni, plat, firma = "Czechitas")
        self.pocet_podr = pocet_podr



    def __str__(self):
        return f"Zamestnanec {self.jmeno}, pozice {self.prac_pozice}, dovolena: {self.pocet_dni}, firma: {self.firma}, pocet podrizenych: {self.pocet_podr} "
    

Klara = Zamestnanec("Klara", "IT support", 25, 60000)
Matej = Zamestnanec("Matej", "Lektor", 20, 30000, "Gopas")
Jana = Manager("Jana", "IT Manager", 30, 70000, 5)

print(Klara.vyuzij_dovolenou(10))
print(Matej.vyuzij_dovolenou(10))
print(Jana.vyuzij_dovolenou(10))