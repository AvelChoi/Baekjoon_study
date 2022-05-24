import sys

input = sys.stdin.readline

# 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M
n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

# 이진탐색 시작점과 끝점이 엇갈리지 않게 종료 조건 설정
while start <= end:
    mid = (start + end) // 2
    count = 0
    count = sum(tree - mid if tree - mid > 0 else 0 for tree in trees)

    if count < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)