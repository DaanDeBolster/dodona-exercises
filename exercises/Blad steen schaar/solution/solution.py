repeat = True
while repeat:
    speler_1 = input()
    speler_2 = input()
    if (speler_1 == 'blad' and speler_2 == 'steen') or (speler_1 == 'steen' and speler_2 == 'schaar') or (speler_1 == 'schaar' and speler_2 == 'blad'):
        print("Speler 1 is gewonnen!")
        repeat = False
    elif (speler_1 == 'blad' and speler_2 == 'schaar') or (speler_1 == 'steen' and speler_2 == 'blad') or (speler_1 == 'schaar' and speler_2 == 'steen'):
        print("Speler 2 is gewonnen!")
        repeat = False
