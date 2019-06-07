N = int(input())
arr = input()
arr = arr.split()
arr = [int(arr[i]) for i in range(N)]

arr.sort()

for k in range(N):
    if k is not 0:
        arr[k] = arr[k-1]+arr[k]

print(sum(arr))