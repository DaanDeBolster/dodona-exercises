Schrijf een programma dat detecteerd of een printer nog voldoende papier heeft. Als invoer neem je twee getallen: Het aantal papieren dat nog in de papierlade zitten, en het aantal papieren dat de volgende afdrukopdracht nodig heeft.

Als er minder papieren in de papierlade zitten dan de afdrukopdracht nodig heeft, geef dan op het scherm `Afdrukopdracht onderbroken: Onvoldoende papier in papierlade.` weer.
In het andere geval, geef dan `Afdrukopdracht voltooid`. Als er na de afdrukopdracht minder dan 100 papieren in de papierlade zitten. Print dan na `Afdrukopdracht voltooid.` ook `Waarschuwing: Nog maar ?? papieren in papierlade.`. Met in plaats van ?? het aantal papieren die na de afdrukopdracht nog overblijven.

## Invoer

- Een geheel getal, het aantal papieren in de papierlade.
- Een geheel getal, het aantal papieren voor de volgende printopdracht.


## Voorbeelden

```
>>> 200
>>> 50
Afdrukopdracht voltooid.

>>> 123
>>> 60
Afdrukopdracht voltooid
Waarschuwing: Nog maar 63 papieren in papierlade.

>>> 94
>>> 100
Afdrukopdracht onderbroken: Onvoldoende papier in papierlade.
```


