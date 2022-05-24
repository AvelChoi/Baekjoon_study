import sys

int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

temp = set(data)

data = sorted(list(temp))

for nums in data:
    print(nums, end=' ')