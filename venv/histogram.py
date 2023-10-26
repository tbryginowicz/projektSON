import matplotlib.pyplot as plt


UsErInPuT = input("Podaj swoj ciąg znakow: ")
scope = input("podaj jakie znaki liczyć odzdzielone ':', jesli wszystkie zostaw puste")
if scope == "":
    scope = UsErInPuT
scope = scope.split(";")
MaP = {}
for c in UsErInPuT:
    if c not in MaP and c in scope:
        MaP[c] = 1
    elif c in scope :
        MaP[c] += 1

print(MaP)

plt.bar(MaP.keys(), MaP.values())
plt.show()
