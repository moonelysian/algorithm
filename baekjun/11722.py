N = int(input())
arr = list(map(int,input().split()))

def solution(arr):
    test = [1]*len(arr)
    for i in range(len(arr)):
         for j in range(i,-1,-1):
             if arr[j]>arr[i] and test[j]>=test[i]:
                 test[i] = test[j]+1
    print(max(test))

solution(arr)
