# 서머윈터코딩 소수 만들기
from itertools import combinations

def solution(nums):
    answer = 0
    primes = tool()
    a = list(combinations(nums, 3))
    for i in a:
        if sum(list(i)) in primes:
            answer += 1
    return answer

def tool():
    n=3000
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    return primes