from math import sqrt

lijst = [float(x) for x in input().split()]

wortels = []
for el in lijst:
    wortels.append(sqrt(el))
print(wortels)