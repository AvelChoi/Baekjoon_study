from collections import deque

n = 7
graph = [[0, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a, b))
    count = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1

    return count


cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for number in cnt:
    print(number)