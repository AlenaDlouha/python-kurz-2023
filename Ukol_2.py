sklad = {
    "1N4148": 250,
    "BAV21": 54,
    "KC147": 147,
    "2N7002": 97,
    "BC547C": 10
}

print(sklad)

soucastka = input("Zadej kod soucastky:")

if soucastka not in sklad:
    print("Součástka není skladem.")
else:
    pocet = int(input("Zadej pocet kusu:"))

    if pocet < 1:
        print("Zadej platný počet kusů.")
    elif sklad[soucastka] < pocet:
        print("Lze vydat pouze omezené množství.")
        print(f"Na skladě je pouze {sklad[soucastka]} kusů.")
    else:
        print("Poptávku lze uspokojit v plné výši.")
        sklad[soucastka] -= pocet

print("Aktuální stav skladu:", sklad)
