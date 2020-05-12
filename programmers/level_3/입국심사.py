def solution(n, times):
    left = 1
    right = max(times)*n # 최악의 경우
    
    while(left <= right):
        average = (left+right)//2
        total = sum([ average//time for time in times ])
        if total < n: # 모든 사람을 심사할 수 없는 경우
            left = average + 1
        else:
            right = average - 1
    return left