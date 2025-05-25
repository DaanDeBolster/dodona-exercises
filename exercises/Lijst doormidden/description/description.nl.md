Schrijf een programma dat twee lijsten van gelijke lengte neemt, en een derde lijst met dezelfde lengte aanmaakt waarvan de linkerhelft dezelfde elementen heeft als lijst 1, en de rechterhelft dezelfde elementen heeft als lijst 2.

## Invoer

- Twee lijsten met gelijke lengte. Je mag ervan uitgaan dat beide lijsten een even aantal elementen bevatten.

## Uitvoer

- De derde lijst zoals hierboven beschreven.

## Opmerking

Start je programma met onderstaande code om aan de gebruiker twee reeksen getallen te vragen, en ze nadien als lijsten in een variabele op te slaan.

```Python
lijst_1 = [x for x in input().split()]
lijst_2 = [x for x in input().split()]
```

## Voorbeeld

```
>>> 1 4 6 9 -5 8 5 2
>>> 7 6 8 2 -6 7 4 1
[1, 4, 6, 9, -6, 7, 4, 1]

>>> True True True True
>>> False False False False
[True, True, False, False]

>>> Dit is de eerste helft 0 0 0 0 0
>>> 0 0 0 0 0 Dit is de tweede helft
["Dit", "is", "de", "eerste", "helft", "Dit", "is", "de", "tweede", "helft"]

```