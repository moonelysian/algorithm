from itertools import permutations
def play(x,y):
    x = list(x)
    y = list(y)
    s = 0
    b = 0
    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i: s+=1
            else: b+=1
    return [s, b]

def solution(baseball):
    v = list(map(lambda x: str(x[0]), baseball))
    r = list(map(lambda x: [x[1], x[2]], baseball))

    lst = list(permutations(range(1,10), 3))
    lst = list(map(lambda x: list(map(str, x)), lst))

    answer = 0

    for x in lst:
        if [play(x,y) for y in v] == r: answer+=1
    return answer

solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])