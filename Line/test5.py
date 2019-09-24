from itertools import permutations

x, y = map(int, input().strip().split(' '))
cony = list(map(int, input().strip().split(' ')))

graph = []

if cony[0]>x or cony[1]>y:
    print("fail")

elif cony==[0,0]:
    print("fail")

else:
    for x in range(cony[0]+1):
        for y in range(cony[1]+1):
            graph.append((x,y))

print(graph)
