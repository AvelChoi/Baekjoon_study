n = int(input())

arr = list(map(int, input().split()))

minn = min(arr)
maxx = max(arr)

print(minn * maxx)