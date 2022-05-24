from sys import stdin

a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

last_win = ''
score = [0, 0]
# score_dict = {'A': 0, 'B': 0, 'D': 0}

for i in range(10):
    if a[i] == b[i]:
        score[0] += 1
        score[1] += 1
    elif a[i] > b[i]:
        score[0] += 3
        last_win = 'A'
    elif a[i] < b[i]:
        score[1] += 3
        last_win = 'B'

print(*score)
if score[0] > score[1]:
    print('A')
elif score[0] < score[1]:
    print('B')
elif len(last_win) > 0:
    print(last_win)
else:
    print('D')