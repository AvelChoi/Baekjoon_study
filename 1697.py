from collections import deque

n, k = map(int, input().split())

graph = [0] * 1000001
count = 0

q = deque()
q.append(n)

while q:
    x = q.popleft()
    count += 1
    
    if x == k:
        break

    # print(f'count: {count}, x: {x}')
    if x > 0:
        if graph[x - 1] == 0:
            q.append(x - 1)
            graph[x - 1] = graph[x] + 1
    if x < 1000000:
        if graph[x + 1] == 0:
            q.append(x + 1)
            graph[x + 1] = graph[x] + 1
    if x < 500000:
        if graph[x * 2] == 0:
            q.append(x * 2)
            graph[x * 2] = graph[x] + 1


print(graph[k])