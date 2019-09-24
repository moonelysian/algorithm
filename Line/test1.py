a,b = map(int, input().strip().split(' '))
arr = []
for i in range(a):
    arr.append(int(input()))

que=[0]*b
count=[1]*b
time = [0]*b

for i in range(b):
    que[i] = arr.pop(0)
    time[i] = que[i]

while len(arr)>0:
    for i in range(b):
        if que[i] == count[i]:
            count[i]=1
            que[i]=arr.pop(0)
            time[i]+=que[i]
        else:
            count[i]+=1

print(max(time))


