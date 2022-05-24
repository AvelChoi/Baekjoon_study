from sys import stdin

input = stdin.readline

m, n = map(int, input().split())

cut = int(input().strip())

# 가로로 자르는 점선은 0과 점선 번호 length
# 세로로 자르는 점선은 1과 점선 번호 width

length = [0]
width = [0]

for _ in range(cut):
    data = list(map(int, input().split()))
    if data[0] == 0:
        length.append(data[1])
    elif data[0] == 1:
        width.append(data[1])

length.sort(), width.sort()

length.append(n), width.append(m)

# print(length, width)

maxx = 0

for i in range(len(length)-1):
    l = length[i+1] - length[i]
    for j in range(len(width)-1):
        w = width[j+1] - width[j]
        
        maxx = max(maxx, l * w)

print(maxx)