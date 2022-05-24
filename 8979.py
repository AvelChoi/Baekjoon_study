# https://pacific-ocean.tistory.com/304

from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

# 번호 순으로 정렬
countries = [list(map(int, input().split())) for _ in range(n)]
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if countries[i][0] == k:
        index = i

for i in range(n):
    if countries[index][1:] == countries[i][1:]:
        print(i+1)
        break