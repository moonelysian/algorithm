N = int(input())
nums = int(input())
arr = []
for i in range(N-1,-1,-1):
    arr.append(nums//10**i)
    if i is not 0:
        nums = nums % (10**i)

print(sum(arr))