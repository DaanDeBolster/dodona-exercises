Schrijf een programma dat alle elementen die niet tot een bepaald interval behoren uit een lijst verwijdert.

## Invoer

- Een lijst met reële getallen.
- Een tweede lijst met twee elementen die een gesloten interval $$[a,b]$$ voorsteld. Ga ervan uit dat $$a<b$$

## Uitvoer

- Een lijst met alle elementen uit de ingevoerde lijst die in $$[a,b]$$ zitten.

## Opmerking

Start je programma met onderstaande code om aan de gebruiker twee reeksen getallen te vragen, en ze nadien als lijsten in een variabele op te slaan.

```Python
lijst = [float(x) for x in input().split()]
interval = [float(x) for x in input().split()]
```

## Voorbeeld

```
>>> 1 4 6 9 -5 8 5 2 2
>>> 2 7
[4.0, 6.0, 5.0, 2.0, 2.0]

>>> 1 4 -10 5 12 -6 -5 -7 -3 0
>>> -5 5
[1.0, 4.0, 5.0, -5.0, -3.0, 0.0]
```