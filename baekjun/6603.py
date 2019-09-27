from itertools import combinations
flage = True

while(flage):
    arr = list(map(int, input().strip().split()))
    N = int(arr[0])
    if N==0:
        flag = False
        break
    
    for case in combinations(arr[1:],6):
        print(' '.join(map(str, case)))
    print('')