from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

q = deque()
q.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


print(graph[n-1][m-1])