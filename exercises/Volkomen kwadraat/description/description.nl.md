Schrijf een programma dat controleert of een getal een volkomen kwadraat is. 

Een volkomen kwadraat $$a$$ is een natuurlijk getal waarvoor een ander natuurlijk getal $$b$$ bestaat zodat $$b^2 = a$$. Bijvoorbeeld $$9$$ is een volkomen kwadraat want $$3^2=9$$.

Of met andere woorden, de vierkantswortel van een volkomen kwadraat is een steeds natuurlijk getal. 

## Invoer

- 1 geheel getal, waarvan je mag uitgaan dat het groter dan nul.

## Uitvoer

- `True` als het ingevoerde getal een volkomen kwadraat is. Anders `False`.

## Opmerking

Schrijf het programma zonder `sqrt` te gebruiken. Een goede methode is een `while`-lus te implementeren die vanaf $$1$$ alle mogelijke natuurlijke getallen tot het ingevoerde getal controleert.

## Voorbeelden

```
>>> 9
True

>>> 25
True

>>> 12
False

>>> 19
False

>>> 100
True
```


