import math

N = int(input())
sit = list(map(int, input().strip().split(' ')))
dist=[]
brown = 0

def distance(p1,p2):
    dx = p1-p2
    return math.sqrt(dx*dx)

if sit.count(0)==1:
    brown=1

elif sit.count(1) == 1:
    dist.append(distance(0, sit.index(1)))
    dist.append(distance(N-1, sit.index(1)))
    brown = int(max(dist))

else:
    for i in range(N):
        if sit[0]==0:
            dist.append(distance(0, sit.index(1)))
        
        if sit[i]!=0:
            for j in range(i+1,N):
                if sit[j]!=0:
                    dist.append(distance(i,j))
                    break
                if sit[N-1]==0:
                    dist.append(distance(i,N-1))
    brown = int(max(dist)//2)
    
print(brown)


            
