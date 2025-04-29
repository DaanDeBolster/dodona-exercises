maxval = float(input())
n = 0
repeat = True
while repeat:
    x = float(input())
    if x == 0:
        repeat = False
    else:
        if x >= maxval:
            n += 1
print(n)