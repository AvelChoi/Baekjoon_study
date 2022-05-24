from sys import stdin
from collections import deque

# 시작 컴퓨터는 1 고정
start = 1
# 컴퓨터의 수
n = int(stdin.readline().strip())
# 컴퓨터의 쌍
com = int(stdin.readline().strip())
# 네트워크가 이어져 있는 관계 1로 표시
network = [[0] * (n+1) for _ in range(n+1)]
# 감염시킬 수 있는 컴퓨터 count로 계산
count = 0

for i in range(com):
    x, y = map(int, stdin.readline().split())
    network[x][y] = network[y][x] = 1


q = deque()
q.append(start)

visited = [0] * (n+1)
visited[start] = 1

while q:
    v = q.popleft()

    for i in range(1, n+1):
        if visited[i] == 0 and network[v][i] == 1:
            visited[i] = 1
            q.append(i)
            count += 1


print(count)