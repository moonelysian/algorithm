#예상 대진표
def solution(n,a,b):
    answer = 0
    
    while (True) :
        if (checkEven(a) == checkEven(b)):
            answer+=1
            break
        answer += 1
        a = checkEven(a)
        b = checkEven(b)

    return answer

def checkEven(num):
    if (num%2 == 0):
        num = num//2
    else:
        num = num//2+1
    return num

solution(8,	4, 7)
