import heapq

def solution(n, works):
    works = [-work for work in works] 
    heapq.heapify(works)

    for i in range(n):
        work = heapq.heappop(works)
        work += 1
        if work > 0:
            work = 0
        heapq.heappush(works, work)

    works = [work*work for work in works]
    return sum(works)
