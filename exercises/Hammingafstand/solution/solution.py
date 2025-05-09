bitsequentie_1 = [int(x) for x in input().split()]
bitsequentie_2 = [int(x) for x in input().split()]

hammingafstand = 0
lengte = len(bitsequentie_1)
for i in range(lengte):
    bit_1 = bitsequentie_1[i]
    bit_2 = bitsequentie_2[i]
    if bit_1 != bit_2:
        hammingafstand += 1
print(hammingafstand)