import sys

n = int(sys.stdin.readline())

data = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x, y])

data = sorted(data, key=lambda x: (x[1], x[0]))

for num in data:
    for m in num:
        print(m, end=' ')