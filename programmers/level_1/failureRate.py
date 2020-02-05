#실패율

def solution(N, stages):
    result = {}
    numOfPlayer = len(stages)
    for stage in range(1, N+1):
        if numOfPlayer!=0:
            count = stages.count(stage)
            result[stage] = count/numOfPlayer
            numOfPlayer -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)

solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])