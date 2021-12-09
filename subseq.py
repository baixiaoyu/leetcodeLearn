
nums = [1, 2, 3, 1]

r = nums



L = [1, 2, 3, 1]
List = [[]]
for i in range(len(L)):
    for j in range(len(List)):
        List.append(List[j] + [L[i]])

print('List =', List)
