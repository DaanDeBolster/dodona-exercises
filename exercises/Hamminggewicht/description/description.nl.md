Een bitsequentie is een reeks opeenvolgende symbolen die ofwel 0 of 1 kunnen zijn. In dit geval spreken we van een lijst die enkel `0` of `1` kan bevatten.

Het Hamminggewicht van een bitsequentie is het aantal keer dat `1` in de bitsequentie voorkomt.

## Invoer

- Een lijst die een bitsequentie voorstelt.

## Uitvoer

- Een geheel getal, het Hamminggewicht.

## Opmerking

Start je programma met onderstaande code om aan de gebruiker een reeks getallen te vragen, en ze nadien als lijst in een variabele op te slaan.

```
bitsequentie = [int(x) for x in input().split()]
```

## Voorbeelden

```
>>> 1 0 1 0 1 1 0
4

>>> 1 1 1 1 1 1 1 1 1 1 0 1
11

>>> 0 0 0 0 0 0
0
```