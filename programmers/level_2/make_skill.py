import math
def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    days = []
    for i in range(N):
        date = math.ceil((100-progresses[i])/speeds[i])
        days.append(date)
    
    temp = 0
    for idx in range(N):
        if days[temp] < days[idx]:
            answer.append(idx-temp)
            temp = idx
    answer.append(N-temp)
    return answer

solution([93,30,55],[1,30,5])