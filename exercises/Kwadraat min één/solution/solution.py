n = int(input())
out = [float(input())]
for i in range(n):
    out.append(out[i]**2-1)
print(out)