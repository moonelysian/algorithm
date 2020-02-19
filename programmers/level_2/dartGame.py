import re

def solution(dartResult):
    exponent = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores = p.findall(dartResult)
    
    for i in range(len(scores)):
        if scores[i][2] == '*' and i > 0:
            scores[i-2] *= 2
        scores[i] = int(scores[i][0])**exponent[scores[i][1]]*option[scores[i][2]]
    return sum(scores)

solution("1S2D*3T")