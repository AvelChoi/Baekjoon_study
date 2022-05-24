from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
  count = 0
  q = deque()

  for i in range(len(graph)):
    for j in range(len(graph[i])):
      if graph[i][j] == 1:
        q.append([i, j])

  while q:
    x, y = q.popleft()
    # print(x, y)
    count += 1
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx > -1 and ny > -1 and nx < n and ny < m:
        if graph[nx][ny] == 0:
          graph[nx][ny] = 1
          q.append([nx, ny])
          

  return count

      
input = stdin.readline

m, n = map(int, input().split())

plate = [list(map(int, input().split())) for i in range(n)]

# print(plate)

print(bfs(plate))