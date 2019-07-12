n = int(input())
arr=[]
for i in range(n):
    num = int(input())
    arr.append(num)
k = int(input())

# Complete the findNumber function below.
def findNumber(arr, k):
    if k in arr:
        print("YES")
    else:
        print("NO")

findNumber(arr, k)