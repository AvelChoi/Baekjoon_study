from sys import stdin

n = int(stdin.readline().strip())
req = list(map(int, stdin.readline().split()))
m = int(stdin.readline().strip())

start, end = 0, max(req)

if sum(req) <= m:
    print(end)
else:
    while start <= end:
        mid = (start + end) // 2
        total = 0

        for r in req:
            total += min(r, mid)
            # print(f'더 작은 값은? min({r}, {mid}) = {min(r, mid)}\ntotal = {total}')

        if total > m:
            end = mid - 1
        elif total <= m:
            start = mid + 1
        # print(f'반복문 마지막 지점, start, end, mid = {start}, {end}, {mid}')

    print(end)