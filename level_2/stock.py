# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
#가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

def solution(prices):
    answer = []
    for i in range(len(prices)):
        time=0   
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time = j-i
                break
        answer.append(time)
    return answer


# 다른 풀이
# from collections import deque

# def solution(prices):
#     answer = []
#     prices = deque(prices)
#     while prices:
#         c = prices.popleft()
#         count = 0
#         for i in prices:
#             if c > i:
#                 count += 1
#                 break
#             count += 1
#         answer.append(count)
#     return answer
