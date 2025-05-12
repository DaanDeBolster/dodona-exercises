lijst = [float(x) for x in input().split()]
interval = [float(x) for x in input().split()]
uitvoer = []
for el in lijst:
    if el >= interval[0] and el <= interval[1]:
        uitvoer.append(el)
print(uitvoer)