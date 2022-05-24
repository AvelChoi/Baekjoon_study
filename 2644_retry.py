from sys import stdin
from collections import deque

# 시작할 숫자 v와 타겟을 함수에 넣어준다
def dfs(v, target):
    visited = [False] * (n+1)
    count = 0
    q = deque([[v, count]])
    # v와 count를 계속 덱에 넣으면서 값을 이어받는다!

    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        
        # 큐에서 popleft한 값이 원하는 촌수에 도달했을 때 종료
        if v == target:
            return count
        
        # 만약 v가 방문하지 않은 곳이라면
        if not visited[v]:
            # 촌수를 더해주고
            count += 1
            # 방문에 True
            visited[v] = True
            # 탐색
            for e in family[v]:
                # 방문하지 않은 곳이면
                if not visited[e]:
                    q.append([e, count])

    return -1


input = stdin.readline

n = int(input().strip())

# 예제 1의 경우 target = [7, 3]
target = list(map(int, input().split()))

m = int(input().strip())

# n = 9, m = 7일때 [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
# family가 어떤 것과 연결되어 있는지 알기 위해서 사용, 따라서 인덱스에 연결된 노드를 넣어줌
family = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

print(dfs(target[0], target[1]))