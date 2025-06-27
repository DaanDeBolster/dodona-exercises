lijst_1 = [x for x in input().split()]
lijst_2 = [x for x in input().split()]
midden = int(len(lijst_1)/2)
print(lijst_1[:midden]+lijst_2[midden:])