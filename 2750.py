import sys

n = int(sys.stdin.readline())
data = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

print('n:', n)
print('data:', data)

for num in data:
    print(num)