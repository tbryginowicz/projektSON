import math
import matplotlib.pyplot as plt

UsErInPuT = input("Podaj swoj ciąg znakow: ")
MaP = {}
for c in UsErInPuT:
    if c not in MaP:
        MaP[c] = 1
    else:
        MaP[c] += 1

print(MaP)

plt.bar(MaP.keys(), MaP.values())
plt.show()
