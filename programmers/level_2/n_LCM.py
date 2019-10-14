def GCD(a, b=None):
    if not b:
        return a
    
    if b>a:
        temp = a
        a = b
        b = temp
    
    while(b>0):
        temp = b
        b = a % b
        a = temp

    return a

def LCM(a, b=None):
    if b == None:
        return a
    
    gcd = GCD(a,b)
    lcm = (a*b//gcd)

    return lcm

def LCMargs(arr):
    currentLCM = None
    for i in arr:
        currentLCM = LCM(i, currentLCM)
 
    return currentLCM
 
 
def GCDargs(arr):
    currentGCD = None
    for i in arr:
        currentGCD = GCD(i, currentGCD)
    return currentGCD


def solution(arr):
    result = LCMargs(arr)
    return result


solution([2,6,8,14])


#최대공약수 함수가 있었다
#from fractions import gcd
#
# def nlcm(num):      
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)

#     return answer

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(nlcm([2,6,8,14]));