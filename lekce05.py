#import swapi

#print(swapi.getPerson(3))

znamky = [0, 2, 3, 1, 1, 3]
pisemky = [
    [1, 3, 2, 1],
    [3, 1, 1, 2],
    [4, 2, 2, 2],
    [1, 1, 1, 1],
    [1, 2, 2, 1],
    [1, 4, 1, 3]
]

nove_znamky = [znamka + 1 for znamka in znamky]
prvni = [z[0] for z in pisemky]

"""
for z in znamky:
    nove_znamky.append(z + 1)

for z in pisemky:
    prvni.append(z[0])
"""

print(f"Stare znamky: {znamky}")
print(f"Nove znakmy: {nove_znamky}")
print(f"prvni: {prvni}")

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]


teploty = [[round(teplota, 2) for teplota in den] for den in teploty]

prumerne_teploty = [round(sum(den) / len(den), 2) for den in teploty]

ranni_teploty = [den[0] for den in teploty]

nocni_teploty = [den[-1] for den in teploty]

poledni_nocni_teploty = [[den[1], den[-1]] for den in teploty]

print("Průměrné teploty pro každý den:", prumerne_teploty)
print("Ranní teploty:", ranni_teploty)
print("Noční teploty:", nocni_teploty)
print("Polední a noční teploty:", poledni_nocni_teploty)


teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]




prumerne_teploty = [round(sum(den) / len(den), 2) for den in teploty]

ranni_teploty = [den[0] for den in teploty]

nocni_teploty = [den[-1] for den in teploty]

poledni_nocni_teploty = [[den[1], den[-1]] for den in teploty]

print("Průměrné teploty pro každý den:", prumerne_teploty)
print("Ranní teploty:", ranni_teploty)
print("Noční teploty:", nocni_teploty)
print("Polední a noční teploty:", poledni_nocni_teploty)