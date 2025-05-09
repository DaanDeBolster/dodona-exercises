Een bitsequentie is een reeks opeenvolgende symbolen die ofwel 0 of 1 kunnen zijn. In dit geval spreken we van een lijst die enkel `0` of `1` kan bevatten.

Gegeven twee bitsequenties met dezelfde lengte. Dan is de Hammingafstand tussen twee bitsequenties het aantal posities met een verschillende bitwaarde.

## Invoer

- 2 lijsten met dezelfde lengte die bitsequenties voorstellen. 

## Uitvoer

- Een geheel getal, de Hammingafstand.

## Opmerking

Start je programma met onderstaande code om aan de gebruiker twee reeksen getallen te vragen, en ze nadien als lijsten in een variabele op te slaan.

```Python
bitsequentie_1 = [int(x) for x in input().split()]
bitsequentie_2 = [int(x) for x in input().split()]
```

## Voorbeelden

```
>>> 1 0 1 0 1 1 0
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