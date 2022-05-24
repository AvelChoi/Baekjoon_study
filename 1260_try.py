from collections import deque
from sys import stdin


def dfs(v):
    dfs_list[v] = 1
    print(v, end=' ')

    for i in range(1, n+1):
        if dfs_list[i] == 0 and graph[v][i] == 1:
            # dfs_list[i] = 1
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        print(v, end=' ')
        bfs_list[v] = 1
        
        for i in range(1, n+1):
            if bfs_list[i] == 0 and graph[v][i] == 1:
                bfs_list[i] = 1
                q.append(i)

                
# 기본 정보 입력받기
n, m, v = map(int, stdin.readline().split())

# graph, 1부터 입력이 들어오므로 n+1 인덱스 활용
graph = [[0] * (n+1) for i in range(n+1)]

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

# visted list
dfs_list = [0] * (n+1)
bfs_list = [0] * (n+1)

# 함수 호출
dfs(v)
print()
bfs(v)