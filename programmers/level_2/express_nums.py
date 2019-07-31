def solution(n):
    answer = len([i for i in range(1,n+1,2) if n%i is 0])
    print(answer)
    return answer

solution(15)