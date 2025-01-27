Schrijf een programma dat een bepaald aantal keer een getal kwadrateerd en er nadien 1 van aftrekt. Het resultaat is een lijst waarin elk element telkens het vorige element in het kwadraat min 1 is. 

## Invoer

- Een positief geheel getal `n`: Het aantal keer dat de kwadratering-min-1-operatie moet worden uitgevoerd.
- Een reëel getal waarop de kwadratering-min-1-operatie `n` keer moet worden uitgevoerd.


## Uitvoer

- Een lijst met lengte `n+1`, waarbij het eerste element het reëel getal is, en elk volgende element gelijk is aan het vorige element, gekwadrateerd min 1.

## Voorbeelden

```
>>> 5
>>> 2
[2, 3, 8, 63, 3968, 15745023]   # 3 = 2^2-1,  8 = 3^2-1, 63 = 8^2-1, ...

>>> 3
>>> -4
[-4, 15, 224, 50175]

>>> 0
>>> 678
[678]
```