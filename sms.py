def over_telefonni_cislo(cislo):
    if len(cislo) == 9 or (len(cislo) == 13 and cislo[:4] == "+420"):
        return True
    else:
        return False

def cena_zpravy(zprava):
    delka_zpravy = len(zprava)
    cena = (delka_zpravy // 180 + 1) * 3
    return cena

def main():
    cislo = input("Zadej telefonní číslo: ")
    if not over_telefonni_cislo(cislo):
        print("Chybný formát telefonního čísla.")
    else:
        zprava = input("Zadej zprávu: ")
        cena = cena_zpravy(zprava)
        print(f"Cena zprávy bude {cena} Kč.")

if __name__ == "__main__":
    main()