lade = int(input())
opdr = int(input())
if opdr > lade:
    print("Afdrukopdracht onderbroken: Onvoldoende papier in papierlade.")
else:
    print("Afdrukopdracht voltooid.")
    if lade - opdr < 100:
        print("Waarschuwing: Nog maar", lade - opdr, "papieren in papierlade.")