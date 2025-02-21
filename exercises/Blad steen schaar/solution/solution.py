getal = int(input())
n = 1
isKwadraat = False
while n**2 <= getal:
    if n**2 == getal:
        isKwadraat = True
    n += 1
print(isKwadraat)