import sys
N = int(input())
numList = [0]*10001

for i in range(N):
    index = int(sys.stdin.readline())
    numList[index] += 1

for num in range(10001):
    sys.stdout.write('%s\n' % num * numList[num])