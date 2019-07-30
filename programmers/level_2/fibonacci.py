def fibonacci(n):
    a,b = 1,0
    for i in range(n):
        a,b = b,a+b
    return b

def solution(n):
    result = fibonacci(n)%1234567
    print(result)
    return result

solution(3)