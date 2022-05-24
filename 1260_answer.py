from collections import deque
from sys import stdin


def bfs(v):
    q = deque()
    q.append(v)

    visited_list_bfs[v] = 1
    
    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in range(1, n + 1):
            # 방문한 적이 없고 그래프 역시 노드가 있는 곳일 때
            if visited_list_bfs[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_list_bfs[i] = 1


def dfs(v):
    # 방문을 표시하고 출력
    visited_list_dfs[v] = 1
    print(v, end=' ')

    for i in range(1, n + 1):
        # 방문한 적이 없고 그래프 역시 노드가 있는 곳일 때
        if visited_list_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)


n, m, v = map(int, stdin.readline().split())

graph = [[0] * (n+1) for _ in range(n+1)]

visited_list_bfs = [0] * (n + 1)
visited_list_dfs = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

# print(graph)


dfs(v)
print()
bfs(v)