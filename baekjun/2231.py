N = int(input())
result = 0
for i in range(1,N+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if( sum_num == N ):
        result = i
        break
print(result)

