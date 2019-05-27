n = int(input())

zero=[1,0]
one=[0,1]

def fibonacci(k):
    for i in range(len(zero),k+1):
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
    print(zero[k],one[k])

for i in range(n):
    k = int(input())
    fibonacci(k)
    