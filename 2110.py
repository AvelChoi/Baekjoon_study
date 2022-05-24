from sys import stdin

input = stdin.readline

n, c = map(int, input().split())

iptime = sorted([int(input().strip()) for _ in range(n)])

start = 1
end = iptime[-1] - iptime[0]

while start <= end:
    mid = (start + end) // 2
    current = iptime[0]
    count = 1

    for i in range(1, len(iptime)):
        if iptime[i] >= mid + current:
            count += 1
            current = iptime[i]

    # 함수로 정확히 리턴하지 않는 이유가 여기에 있다
    # mid를 최대한으로 늘려야 하고, start가 end보다 커지기 직전까지 계속 돌려야 하기 때문
    # 그렇기에 종료조건이 확실한 while문을 사용하는게 차라리 낫다.
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)