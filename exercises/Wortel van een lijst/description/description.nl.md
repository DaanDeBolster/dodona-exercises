Schrijf een programma dat een lijst als invoer neemt, en een nieuwe lijst teruggeeft met de vierkantswortels van de elementen uit de ingevoerde lijst.

## Invoer

- Een lijsten met positieve reële getallen.

## Uitvoer

- Een lijsten met positieve reële getallen, de vierkantswortels van de getallen uit de eerste lijst.

## Opmerking

Start je programma met onderstaande code om aan de gebruiker een reeksen getallen te vragen, en ze nadien als lijst in een variabele op te slaan.

```Python
lijst = [float(x) for x in input().split()]
```

## Voorbeelden

```
>>> 1 0 1 0 1 1 0
0

>>> 0 1 1 0 0 0 0 1
>>> 1 0 0 1 1 1 1 0
8

>>> 0 1 1 1 1 0
>>> 0 0 1 0 0 1
4

>>> 0 0 1 0 1
>>> 0 1 0 0 1
2
```