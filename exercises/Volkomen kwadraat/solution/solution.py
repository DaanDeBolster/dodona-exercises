bedrag = float(input())
eraf = float(input())

if bedrag - eraf < 0:
    print("Saldo ontoereikend")
else:
    print(bedrag -eraf, "op rekening")