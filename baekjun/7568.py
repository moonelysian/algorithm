N = int(input())

person =[ list(map(int, input().split())) for _ in range(N) ]

rank = [1]*N

for i in range(N):
    for j in range(N):
        if person[i][0] != person[j][0] and person[i][1] != person[j][1]:
            if person[i][0] > person[j][0] and person[i][1] > person[j][1]:
                rank[j] += 1

rank = [ str(rank[i]) for i in range(N)]

print(' '.join(rank))