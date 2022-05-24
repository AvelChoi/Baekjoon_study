from sys import stdin

input = stdin.readline

n = int(input())

color_paper = [[0] * 1002 for _ in range(1002)]
# color_paper = [[0] * 15 for _ in range(15)]

max_num = 0

for i in range(n):
    paper = list(map(int, input().split()))
    x1, y1, x2, y2 = paper[0], paper[1], paper[2], paper[3]
    max_num = max(max_num, x1, y1, x1+x2, y1+y2)

    for j in range(y1, y1 + y2):
        for k in range(x1, x1 + x2):
            color_paper[j][k] = i+1

for i in range(n):
    count = 0
    for j in range(max_num+1):
        for k in range(max_num+1):
            if color_paper[j][k] == i+1:
                count += 1
    
    print(count)