N = int(input())
count = 1

if not (0 <= N <= 99):
    exit()

input_num = N

while True:
    back = N%10
    N = (back*10) + (N//10 + back)%10

    if (input_num == N):
        break
    else:
        count += 1

print(count)