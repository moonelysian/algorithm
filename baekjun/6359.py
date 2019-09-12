N = int(input())
domLen = []
for n in range(N):
    n = int(input())
    domLen.append(n)

def solution(domLen):
    for length in domLen:
        count = 0
        for n in range(1,length+1):
            if n*n <= length:
                count+=1
        print(count)

solution(domLen)

