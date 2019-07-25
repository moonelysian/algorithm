N = list(map(int,input()))
N.sort(reverse=True)
result = ''
for i in N:
    result += str(i)

print(int(result))