from sys import stdin
from collections import deque

n = int(stdin.readline().strip())

target_a, target_b = map(int, stdin.readline().split())

m = int(stdin.readline().strip())

family = [[0] * (n+1) for _ in range(n+1)]

# 원래 썼던 코드
# for _ in range(m):
#     x, y = map(int, stdin.readline().split())
#     family[x][y] = family[y][x] = 1

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    family[x].append(y)
    family[y].append(x)

visited = [0] * (n+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        node = q.popleft()

        for i in family[node]:
            if visited[i] == 0:
                # visted 리스트에 0, 1로 방문만 표시하는 것이 아닌 촌수를 기입
                visited[i] += (visited[node] + 1)
                q.append(i)

bfs(target_a)

if visited[target_b] != 0:
    print(visited[target_b] - 1)
else:
    print(-1)