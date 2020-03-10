def solution(n, computers):
    visited = [0] * n
    answer = 0

    def dfs(computers, visited, startNode):
        stack = [startNode]
        while stack:
            i = stack.pop()
            if visited[i] == 0:
                visited[i] = 1
            for j in range(len(computers)):
                if computers[i][j] == 1 and visited[j] == 0:
                    stack.append(j)
    
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i+=1
    return answer