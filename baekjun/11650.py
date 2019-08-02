from sys import stdin

read = lambda : stdin.readline().strip()

ans = []
for _ in range(int(read())):
    x, y = map(int, read().split())
    ans.append((x, y))

for x, y in sorted(ans):
    print(x, y)
