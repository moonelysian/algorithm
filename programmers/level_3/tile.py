def solution(N):
    x = fibonacci(N+1)
    y = fibonacci(N)
    answer = (x+y) * 2
    return answer

def fibonacci(num): 
    a, b = 0, 1 
    
    for i in range(num): 
        a, b = b, a+b 
    return a

solution(5)