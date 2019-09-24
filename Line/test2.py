from itertools import permutations

arr = list(map(int, input().strip().split(' ')))
index = int(input())
test = list(permutations(arr,len(arr)))

result = []
for item in test:
    c=""
    for i in range(len(item)):
        c += str(item[i])
    result.append(c)

result.sort()
print(result[index-1])