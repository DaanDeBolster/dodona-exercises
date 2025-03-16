Schrijf een programma dat in een drankautomaat begeleid als iemand een drankje wil kopen. Als invoer neem je twee getallen: De kostprijs van een drankje, en het bedrag dat iemand als krediet aan de drankautomaat heeft betaald.

Als het krediet kleiner is dan de kostprijs van het drankje, geef dan op het scherm `Transactie onderbroken: Onvoldoende krediet.` weer.
In het andere geval, geef dan `Transactie voltooid: Bedankt voor uw aankoop.`. Als er na de transactie nog krediet over is, print dan na `Transactie voltooid: Bedankt voor uw aankoop.` ook `Nog ?? krediet resterend.`. Met in plaats van ?? het krediet dat na de transactie overblijft.

## Invoer

- Een reëel getal, de kostprijs van een drankje.
- Een reëel getal, het krediet, het bedrag dat de gebruiker heeft ingeworpen.


## Voorbeelden

```
>>> 2.5
>>> 2.5
Transactie voltooid: Bedankt voor uw aankoop.

>>> 3.4
>>> 5
Transactie voltooid: Bedankt voor uw aankoop.
Nog 1.6 krediet resterend.

>>> 2.4
>>> 2
Transactie onderbroken: Onvoldoende krediet.
```


