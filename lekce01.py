""" print("Vitejte v kurzu Pythonu")

nazev_hry = "Romeo a Julie"
cena_listku = 150
pocet_listku = int(input("Zadejte prosim pocet listku:"))

celkova_cena = cena_listku * pocet_listku

#Pokud je pocet listku 3, dostane zakaznik slecvu 10%

if pocet_listku >= 3:
    zlevnena_cena = celkova_cena * 0.90
    print(f"Zlevnena cena je {zlevnena_cena} z původní ceny {celkova_cena}")
else:
    print(f"Celkova cena je {celkova_cena}") """

""" 
print("Dobrý" + " " + "den")
pozdrav = 1
print(f"Pozdrav je {pozdrav}")
venecky = [1, 2, 1, 2, 6, 3, 2]

# spojovani sekvenci
print("Pozdrav je" + str(pozdrav))
print(venecky + [0,1,2,3,5,6,4])
print(pozdrav) """

# slicing - souvisí s indexovanim v ramci sekvenci
jmeno = "Alena"
print(jmeno[1])
print(jmeno[2])
print(jmeno[-2])

venecky = [1, 2, 1, 2, 6, 3, 2]
# od pondeli do patku
#syntax venecky[zacatek:konec+1]
print(venecky[0:5])

#od utery do soboty
print(venecky[1:6])

# od utery do konce tydne
print(venecky[1:])

# od zacatku do ctvrtka
print (venecky[:4])

jmeno = "Andy Novakova"
print(jmeno[:4])
print(jmeno[5:])