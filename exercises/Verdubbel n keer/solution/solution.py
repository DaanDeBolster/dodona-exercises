lijst_1 = [x for x in input().split()]
lijst_2 = [x for x in input().split()]
helft = len(lijst_1)//2
lijst_3 = lijst_1[:helft] + lijst_2[helft:]
print(lijst_3)