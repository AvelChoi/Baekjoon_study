from sys import stdin

testcase = int(stdin.readline().strip())

# 테스트 케이스 만큼 반복
for _ in range(testcase):
    ppl = int(stdin.readline().strip())
    count = 1
    newface = []
    for _ in range(ppl):
        nf = list(map(int, stdin.readline().split()))
        newface.append(nf)

    # 정렬 후 1번을 기준(Max)으로 삼고 비교
    newface.sort()
    Max = newface[0][1]

    for i in range(1, ppl):
        if Max > newface[i][1]:
            count += 1
            Max = newface[i][1]
    
    print(count)