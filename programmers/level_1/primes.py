#문제
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

#내 풀이
def solution(n):
    nums = [False,False] + [True]*(n-1)
    answer = []
    
    for i in range(2,n+1):
        if nums[i]:
            answer.append(i)
            for j in range(i*2,n+1,i): #에라토스테네스의 체
                nums[j] = False
    return len(answer)

# 다른 사람 풀이
# def solution(n):
#     num=set(range(2,n+1))
#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)