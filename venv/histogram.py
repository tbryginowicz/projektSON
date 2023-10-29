import matplotlib.pyplot as plt


print("MENU\n1. Licz wszystkie znaki\n2. Licz podane znaki\n3. Wyjscie")
MeNuInPuT = input(": ")

if MeNuInPuT == "1":
    UsErInPuT = input("Podaj swoj ciąg znakow: ")
    MaP = {}
    for c in UsErInPuT:
        if c not in MaP:
            MaP[c] = 1
        else:
            MaP[c] += 1

elif MeNuInPuT == "2":

    UsErInPuT = input("Podaj swoj ciąg znakow: ")
    scope = input("podaj jakie znaki liczyć odzdzielone ':', jesli wszystkie zostaw puste")
    if scope == "":
        scope = UsErInPuT
    else:
        scope = scope.split(";")
    MaP = {}
    for c in UsErInPuT:
        if c not in MaP and c in scope:
            MaP[c] = 1
        elif c in scope:
            MaP[c] += 1

elif MeNuInPuT == "3":
    exit()


print(MaP)

plt.bar(MaP.keys(), MaP.values())
plt.show()
