prijs = float(input())
krediet = float(input())
if prijs > krediet:
    print("Transactie onderbroken: Onvoldoende krediet.")
else:
    print("Transactie voltooid: Bedankt voor uw aankoop.")
    if prijs < krediet:
        print("Nog", krediet - prijs, "krediet resterend.")