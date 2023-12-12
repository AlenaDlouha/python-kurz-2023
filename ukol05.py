teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Seznam průměrných teplot pro každý den
prumerne_teploty = [sum(den) / len(den) for den in teploty]

# Seznam ranních teplot
ranni_teploty = [den[0] for den in teploty]

# Seznam nočních teplot
nocni_teploty = [den[-1] for den in teploty]

# Seznam dvouprvkových seznamů pro polední a noční teplotu
poledni_nocni_teploty = [[den[1], den[-1]] for den in teploty]

print("Průměrné teploty pro každý den:", prumerne_teploty)
print("Ranní teploty:", ranni_teploty)
print("Noční teploty:", nocni_teploty)
print("Polední a noční teploty:", poledni_nocni_teploty)


