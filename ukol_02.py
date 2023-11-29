sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

print(sklad)

soucastka = input("Zadej kod soucastky:")
pocet = int(input("Zadej pocet kusu:"))

print(soucastka,pocet)


if soucastka not in sklad:
        print("Součástka není skladem")
else:
    pocet_soucastek_skladem = sklad[soucastka]
    if pocet_soucastek_skladem < pocet:
        print("Lze vydat pouze omezené množství")
        del sklad[soucastka]
    elif pocet_soucastek_skladem >= pocet:
        print("Poptávku lze uspokojit v plné výši")
        sklad[soucastka] -= pocet

print()


