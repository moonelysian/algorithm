chess = []
for i in range(8):
    chess.append(input())
print(chess)
num = 0

for i in range(8):
    if i%2 is 0:
        for j in range(0,8,2):
           if chess[i][j] is 'F':
               num += 1
    else:
        for j in range(1,8,2):
            if chess[i][j] is 'F':
                num += 1

print(num) 