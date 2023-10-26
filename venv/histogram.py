import matplotlib.pyplot as plt

toJeszczeDoUstalenia = input("Wpisz cos: ")
slownikNazwaDoUstalenia = {}

for zmiennaDoUstalenia in toJeszczeDoUstalenia:
    if zmiennaDoUstalenia not in slownikNazwaDoUstalenia:
        slownikNazwaDoUstalenia[zmiennaDoUstalenia] = 1
    else:
        slownikNazwaDoUstalenia[zmiennaDoUstalenia] += 1

print(slownikNazwaDoUstalenia)

plt.bar(slownikNazwaDoUstalenia.keys(), slownikNazwaDoUstalenia.values())
plt.show()
