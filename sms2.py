def over_telefonni_cislo(cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13 and cislo[:4] == "+420":
        return True
    else:
        return False

def cena_zpravy(zprava):
    delka_zpravy = len(zprava)
    pocet_zprav = delka_zpravy // 180 + 1
    cena = pocet_zprav * 3
    return cena

def zadani_zpravy():
    cislo = input("Zadej telefonní číslo: ")
    if not over_telefonni_cislo(cislo):
        print("Chybný formát telefonního čísla.")
    else:
        zprava = input("Zadej zprávu: ")
        cena = cena_zpravy(zprava)
        print(f"Cena zprávy bude {cena} Kč.")

zadani_zpravy()  # Tento řádek zavolá funkci při spuštění skriptu