from sys import stdin

input = stdin.readline

n = int(input().strip())

ropes = sorted([int(input().strip()) for _ in range(n)], reverse=True)

max_weight = 0

for i, rope in enumerate(ropes):
    max_weight = max(max_weight, rope * (i+1))

print(max_weight)