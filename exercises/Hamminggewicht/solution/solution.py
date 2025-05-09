bitsequentie = [int(x) for x in input().split()]

hamminggewicht = 0
for bit in bitsequentie:
    if bit == 1:
        hamminggewicht += 1
print(hamminggewicht)