import re

def solution(dartResult):
    answer = 0
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores = p.findall(dartResult)
    result = []
    for idx, score in enumerate(scores):
        point = int(score[0])
        exponent = score[1]
        option = score[2]

        if (exponent == 'S'):
            exponent = 1
        elif (exponent == 'D'):
            exponent = 2
        elif (exponent == 'T'):
            exponent = 3
        if (option == '*'):
            if (idx == 0):
                result.append(point**exponent*2)
            else:
                result[-1] *= 2
                result.append(point**exponent*2)
        elif option == '#':
            result.append(point**exponent*-1)
        else: result.append(point**exponent)
    return sum(result)

solution("1S2D*3T")