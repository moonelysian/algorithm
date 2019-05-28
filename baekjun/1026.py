n = int(input())
s = 0

A = input()
B = input()

A = A.split()
B = B.split()

A = [ int(A[i]) for i in range(n) ]
B = [ int(B[i]) for i in range(n) ]

A.sort(reverse=True)
B.sort()

for i in range(n):
    s += A[i]*B[i]

print(s)
    
