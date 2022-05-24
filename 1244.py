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
# students = [list(map(int, input().split())) for _ in range(s)]

# for student in students:
    # sex = student[0]
    # target = student[1]

for _ in range(s):
    sex, target = map(int, input().split())

    if sex == 1:
        for i in range(target, len(status)+1, target):
            status[i-1] = change(status[i-1])

    elif sex == 2:
        target -= 1
        
        # status[target] = change(status[target])
        if status[target] == 1:
            status[target] = 0
        else:
            status[target] = 1

        left = target - 1
        right = target + 1
        
        while left >= 0 and right < n and status[left] == status[right]:
            if status[left] == 0:
                status[left], status[right] = 1, 1
            elif status[left] == 1:
                status[left], status[right] = 0, 0

            left -= 1
            right += 1

            if left < 0 or right >= n:
                break

        # 실패한 코드
        # for i in range(1, n//2):
            # if target - i < 0 or target - i >= n or target + i >= n or target + i < 0:
            # if 0 > target - i >= n and 0 > target + i >= n:
        #         break

        #     if status[target - i] == status[target + i]:
        #         # print(status[target + i], status[target - i], '같음')
        #         if status[target + 1] == 0:
        #             status[target + i] = status[target - i] = 1
        #         else:
        #             status[target + i] = status[target - i] = 0

for i in range(0, n, 20):
    print(*status[i:i+20])