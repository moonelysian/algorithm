N = int(input())
arr = list(map(int,input().split()))

def getGCD(a,b):
    while(b>0):
        tmp=a
        a=b
        b=tmp%b
    return a


for i in range(1,N):
    gcd = getGCD(max(arr[0],arr[i]),min(arr[0],arr[i]))
    print(str(int(arr[0]/gcd)) + "/" + str(int(arr[i]/gcd)))