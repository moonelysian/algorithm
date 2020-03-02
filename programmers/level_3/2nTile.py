# 2xn타일링
def solution(n):
    answer = fibo(n) % 1000000007
    print(answer)
    return answer

def fibo(num):
    a, b = 0, 1 
    for i in range(num+1): 
        a, b = b, a+b 
    return a

solution(4)
