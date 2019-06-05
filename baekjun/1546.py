N = int(input())
scores = input()
scores = scores.split()
scores = [int(scores[i]) for i in range(N)]

m = max(scores)

for i in range(N):
    scores[i] = scores[i]/m*100

print(sum(scores)/N)

