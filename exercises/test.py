repeat = True
a = float(input("Geef een getal."))
b = float(input("Geef nog een getal."))
while a < b:
    if a < b:
        a += 1
        repeat = True
        print(a)
    else:
        repeat = False
        print(a)