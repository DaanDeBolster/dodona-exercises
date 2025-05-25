lijst_1 = [x for x in input().split()]
lijst_2 = [x for x in input().split()]
print(lijst_1[:int(len(lijst_1)/2)+1]+lijst_2[int(len(lijst_2)/2+1):])