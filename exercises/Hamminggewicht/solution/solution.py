bitstr = input()
hamming = 0
for bit in bitstr:
    if bit != '0':
        hamming += 1
print(hamming) 