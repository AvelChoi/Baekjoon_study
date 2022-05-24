import sys

sys_input = sys.stdin.readline

# 시간 변환이 너무 많이 나와서 함수로 제작
def hour(number):
    return int(number[:2] + number[3:])

s, e, q = map(str, sys_input().split())
s, e, q = hour(s), hour(e), hour(q)

check = set()
count = 0

while True:
    try:
        time, name = map(str, sys_input().split())
        time = hour(time)

        if time <= s:
            check.add(name)

        if e <= time <= q and name in check:
            check.remove(name)
            count += 1
        
    except:
        break

print(count)