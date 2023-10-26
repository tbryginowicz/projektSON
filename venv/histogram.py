import matplotlib.pyplot as plt


print("MENU\n1. Licz wszystkie literki\n2. Licz podana literke\n3. Wyjscie")
MeNuInPuT = input(": ")

if MeNuInPuT == "1":
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
        elif c in scope :
            MaP[c] += 1

elif MeNuInPuT == "2":
    LiTeRkAdOpOlIcZeNiA = input("Jaka literke liczyc: ")
    UsErInPuT = input("Podaj swoj ciąg znakow: ")
    scope = input("podaj jakie znaki liczyć odzdzielone ':', jesli wszystkie zostaw puste")
    if scope == "":
        scope = UsErInPuT
    else:
        scope = scope.split(";")
    MaP = {}
    for c in UsErInPuT:
        if c not in MaP and c in scope and c == LiTeRkAdOpOlIcZeNiA:
            MaP[c] = 1
        elif c in scope and c == LiTeRkAdOpOlIcZeNiA:
            MaP[c] += 1

elif MeNuInPuT == "3":
    exit()


print(MaP)

plt.bar(MaP.keys(), MaP.values())
plt.show()
