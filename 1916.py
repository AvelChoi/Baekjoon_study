import sys
from heapq import heappush, heappop

def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start))
    # 각 정점 사이의 거리를 무한대로 초기화
    distance = [sys.maxsize] * (n + 1)
    distance[start] = 0

    while heap:
        weight, index = heappop(heap)
        for e, c in bus_route[index]:
            if distance[e] > weight + c:
                distance[e] = weight + c
                heappush(heap, (weight + c, e))
    return distance[end]


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input().strip())
    m = int(input().strip())

    bus_route = [[] for _ in range(n+1)]

    for _ in range(m):
        start, end, pay = map(int, input().split())
        # bus_route[start][end] = bus_route[end][start] = pay
        bus_route[start].append((end, pay))


    t1, t2 = map(int, input().split())

    print(dijkstra(t1, t2))

# https://jjangsungwon.tistory.com/28