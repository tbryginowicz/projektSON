import math
import matplotlib.pyplot as plt

input = input("Podaj swoj ciąg znakow: ")
map = {}
for c in input:
    if c not in map:
        map[c] = 1
    else:
        map[c] += 1

print(map)

plt.bar(map.keys(), map.values())
plt.show()
