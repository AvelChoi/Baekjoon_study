from sys import stdin

input = stdin.readline

n = int(input().strip())

students = [list(map(int, input().split())) for _ in range(n)]
check_list = [[] for _ in range(n)]
print(check_list)

# 원래 학생 i
for i in range(n):
    # 비교할 학생 j
    for j in range(n):
        # 자기 자신을 비교 불가
        if i == j:
            continue
        else:
            for k in range(len(students[i])):
                if students[i][k] == students[j][k] and j+1 not in check_list[i]:
                    check_list[i].append(j+1)
    


print(check_list)

maxx = 0

for i in range(1, len(check_list)):
    if len(check_list[maxx]) < len(check_list[i]):
        maxx = i

print(maxx+1)