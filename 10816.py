import sys

n = sys.stdin.readline()

cards = list(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline()

numbers = list(map(int, sys.stdin.readline().split()))

sample_list = [0] * 20000001

for card in cards:
    sample_list[card+10000000] += 1

for num in numbers:
    print(sample_list[num+10000000], end=' ')


# 메모리 242080KB 시간 1100ms