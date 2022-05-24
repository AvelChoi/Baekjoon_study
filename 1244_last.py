from sys import stdin

def change(num):
    if num == 0:
        return 1
    else:
        return 0

input = stdin.readline

n = int(input().strip())
status = list(map(int, input().split()))
s = int(input().strip())
students = [list(map(int, input().split())) for _ in range(s)]

for student in students:
    sex = student[0]
    target = student[1]

    if sex == 1:
        for i in range(target, len(status)+1, target):
            status[i-1] = change(status[i-1])

    elif sex == 2:
        target -= 1

        if status[target] == 1:
            status[target] = 0
        else:
            status[target] = 1

        for i in range(1, n//2):
            if 0 <= target - i < n and 0 <= target + i < n:
                if status[target - i] == status[target + i]:
                # print(status[target + i], status[target - i], '같음')
                    if status[target + 1] == 0:
                        status[target + i] = status[target - i] = 1
                    else:
                        status[target + i] = status[target - i] = 0
                

for i in range(0, n, 20):
    print(*status[i:i+20])