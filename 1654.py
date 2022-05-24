from sys import stdin

input = stdin.readline

k, n = map(int, input().split())

cables = [int(input().strip()) for _ in range(k)]

answer = 0

# 이진탐색
start = 1
end = max(cables)
able_max = sum(cables) // n

while start <= end:
    count = 0
    mid = (start + end) // 2
    if mid == 0:
        answer = 1
        break
    print('mid:', mid)
    
    for c in cables:
        count += c // mid
        print('count:', count)

        if count >= n and mid > answer:
            answer = mid
            break
    
    if count < n:
        end = mid - 1
    else:
        start = mid + 1

print(answer)