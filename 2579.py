from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = stdin.readline

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = -1

area = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            area_count = 1
                
            q = deque()
            q.append([i, j])
            graph[i][j] = 1

            while q:
                x, y = q.popleft()
                
                for u in range(4):
                    nx = x + dx[u]
                    ny = y + dy[u]

                    if nx >= 0 and ny >= 0 and nx < m and ny < n and graph[nx][ny] == 0:
                        area_count += 1
                        graph[nx][ny] = 1
                        q.append([nx, ny])
            
            area.append(area_count)

print(len(area))
print(*sorted(area), sep=' ')