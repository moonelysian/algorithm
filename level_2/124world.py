# 124 나라의 숫자
# 문제 설명
# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.

def solution(n):
    answer = ''
    while(n>0):
        mod = n%3
        n//=3
        if mod is 0:
            n-=1
        answer = '412'[mod] + answer
    return answer

solution(5)