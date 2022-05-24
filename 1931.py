from sys import stdin

n = int(stdin.readline().strip())

meets = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    meets.append([a, b])

# 끝나는 시각을 우선시 하되, 끝나는 시각을 함께 고려한 결과 풀림
# 반례 https://www.acmicpc.net/board/view/81289 참고
meets = sorted(meets, key=lambda x: (x[1], x[0]))
now = 0
count = 0

for i in range(len(meets)):
    print('for문 인덱스 i:', i)

    if meets[i][0] >= now:
        print('조건문 진입')
        for j in range(i, len(meets)):
            print(f'{j}번째 도는 중, meets[i][1] < meets[j][1]: {meets[i][1]} <= {meets[j][1]} ?')
            if meets[i][1] > meets[j][1]:
                continue
            else:
                count += 1
                now = meets[i][1]
                print(f'{j} 조건문 진입, now = {now}, count = {count}, i = {meets[i]}')
                break

print(count)