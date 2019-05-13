# 그룹별로 4인용 택시 타기
s = [2,3,4,4,2,1,3,1]
taxi =  0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]+s[j] == 4):
            taxi+=1
            s[i]=0
            s[j]=0
            break
tmp = list(set(s))
tmp.remove(0)
taxi += len(tmp)
print(taxi)