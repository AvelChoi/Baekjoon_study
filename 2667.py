from collections import deque

# n = int(input())

# graph = []
# [graph.append(list(map(int, input()))) for _ in range(n)]

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

numbering = 1

house = []

q = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i, j))
            count = 0
            
            while q:
                x, y = q.popleft()

                graph[x][y] = 0
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx >= 0 and ny >= 0 and nx < n and ny < n:
                        q.append((nx, ny))
                        count += 1
                
            house.append(count)


print(house)