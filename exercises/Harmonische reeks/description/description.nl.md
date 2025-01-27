De harmonische reeks neemt de som van de eerste `n` omgekeerde getallen. Zo is... <br>
$$h_1 = \frac{1}{1}$$ <br>
$$h_2 = \frac{1}{1}+\frac{1}{2}$$ <br>
$$h_3 = \frac{1}{1}+\frac{1}{2}+\frac{1}{3}$$ <br>
$$h_4 = \frac{1}{1}+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}$$ <br>
... <br>
$$h_n = \frac{1}{1}+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+...+\frac{1}{n}$$ <br>

Schrijf een recursieve functie `harmonisch` die het `n`-de getal uit de Harmonische reeks berekend.

## Argumenten

- Een geheel getal `n`, waarvan je mag veronderstellen dat het niet `0` of negatief kan zijn.

## Returnwaarde

- Een reëel getal: het `n`-de getal uit de harmonische reeks.

## Voorbeelden

```
>>> harmonisch(1)
1.0

>>> signum(2)
1.5

>>> signum(6)
2.45
```