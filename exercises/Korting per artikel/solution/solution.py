prijzen = [float(x) for x in input().split()]
aantallen = [int(x) for x in input().split()]
kortingspercentages = [float(x) for x in input().split()]

totale_prijs = 0
totale_korting = 0
aantal_artikelen = len(prijzen)

for i in range(aantal_artikelen):
    prijs = prijzen[i]
    aantal = aantallen[i]
    kortingspercentage = kortingspercentages[i]
    totale_prijs += prijs * aantal
    totale_korting += prijs * aantal * kortingspercentage/100

print("Totale prijs zonder korting:", totale_prijs)
print("Totale korting:", totale_korting)
print("Totale prijs met korting:", totale_prijs - totale_korting)