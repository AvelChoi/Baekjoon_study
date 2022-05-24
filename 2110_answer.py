from sys import stdin

def binary_search(data, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = data[0]
        count = 1

        for i in range(1, len(data)):
            if data[i] >= current + mid:
                count += 1
                current = data[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


input = stdin.readline

n, c = map(int, input().split())

iptime = sorted([int(input().strip()) for _ in range(n)])

binary_search(iptime, 1, int(iptime[-1] - iptime[0]))
print(answer)