#summer code..!
#올바른 괄호 만들 수 있는 경우의 수
#카탈란 수

def solution(N):
    result  = []
    count = 0
    cal(result,"",0,0,N,count)

    print(result)

def cal(result, cur, start, end, n , count):
    if(len(cur) == n*2):
        result.append(cur)
        return
    if(start<n):
        cal(result, cur + "(", start+1, end, n , count+1)
    if(end<start):
        cal(result, cur + ")", start, end+1, n , count+1 )