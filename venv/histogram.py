import math
import matplotlib.pyplot as plt

inputString = input("Podaj swoj ciąg znakow: ")
scope = input("podaj jakie znaki liczyć odzdzielone ':', jesli wszystkie zostaw puste")
if scope == "":
    scope = inputString
scope = scope.split(";")

map = {}
for c in inputString :
    if c not in map and c in scope:
        map[c] = 1
    elif c in scope :
        map[c] += 1

print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")
print("KONFLIKT")

print(map)

plt.bar(map.keys(), map.values())
plt.show()
