Implementeer een programma dat een kortingspercentage toepast op een reeks artikelen in een winkel.

Het programma vraagt aan de gebruiker drie lijsten van gelijke lengte: 
- De eerste lijst bevat de prijs van elk artikel dat een klant heeft gekocht.
- De tweede lijst bevat voor elk artikel het aantal dat de gebruiker heeft gekocht.
- De derde lijst bevat hoeveel procent korting op het huidige moment van toepassing is bij elk artikel. Als er geen korting van toepassing is bevat de lijst `0`.

Op het einde geef je aan de gebruiker drie getallen terug:
- De totale prijs zonder korting
- De totale korting op alle aangeschafte artikelen
- De totale prijs met korting

## Invoer

- 3 lijsten met dezelfde lengte zoals hierboven beschreven

## Uitvoer

- "Totale prijs zonder korting: ...>"
- "Totale korting: ...>"
- "Totale prijs met korting: ...>"

## Opmerking

Start je programma met onderstaande code om aan de gebruiker drie reeksen getallen te vragen, en ze nadien als lijsten in een variabele op te slaan.

```Python
prijzen = [float(x) for x in input().split()]
aantallen = [int(x) for x in input().split()]
kortingspercentages = [float(x) for x in input().split()]
```

## Voorbeelden

```
>>> 1.9 2.1 4   1.6
>>> 1   1   3   2
>>> 0   0   20  50
Totale prijs zonder korting: 19.2
Totale korting: 4.0
Totale prijs met korting: 15.2
```