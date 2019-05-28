# 가장 큰 수
# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
# 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

def max_(a,b):
    return a<=b if len(a)==len(b) else a+b <= b+a 

def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        tmp = arr[0]
        big = [i for i in arr[1:] if max_(i, tmp)]
        small = [i for i in arr[1:] if not max_(i, tmp)]
        return quick_sort(small) + [tmp] + quick_sort(big)


def solution(numbers):
    if set(numbers) == {0}:
        return "0"
    numbers = [str(num) for num in numbers]
    numbers = quick_sort(numbers)
    answer = "".join(numbers)
    return answer

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True) #x*3인 이유: 자리수가 1000이하이기 때문
#     return str(int(''.join(numbers)))

solution([3, 30, 34, 5, 9])