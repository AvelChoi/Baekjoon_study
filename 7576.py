from sys import stdin
from collections import deque

def bfs(graph, m, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    empty_count = 0
    aged_count = 0
    day = 0

    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append([i, j])
            elif graph[i][j] == -1:
                empty_count += 1
    
    if len(q) > 0 and (n * m) == len(q) + empty_count:
        return 0
    
    while q:
        x, y = q.popleft()
        aged_count += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])
                    day = max(day, graph[nx][ny])
    
    # 96%, 99%에서 자꾸 오류가 발생했는데, 익은 토마토가 하나도 없는 경우를 대비하지 않았었음                
    if aged_count > 0 and (empty_count + aged_count) == (n * m):
        return day - 1
    else:
        return -1
            

input = stdin.readline
m, n = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(n)]

print(bfs(plate, m, n))