from sys import stdin

def solution(p, n, numbers):
    if n == 0:
        numbers = []
    
    # left, right 변수를 이용해 인덱스를 조절
    # 실제로 pop과 같은 연산을 거치지 않더라도 비슷한 효과를 낼 수 있다.
    l, r, re = 0, 0, True

    for process in p:
        if process == 'R':
            # re 변수를 통해 뒤집는지 판별
            re = not re
        else:
            if re is True:
                l += 1
            else:
                r += 1
    
    if r + l <= n:
        answer = numbers[l:n - r]

        # 정방향일 경우 그대로 출력
        if re is True:
            return '[' + ','.join(answer) + ']'
        # 뒤집혔을 경우 바꾸기
        else:
            return "[" + ",".join(answer[::-1]) + "]"
    else:
        return 'error'


T = int(input())

for _ in range(T):
    p = list(stdin.readline().strip())
    n = int(stdin.readline().strip())
    num = stdin.readline().strip()[1:-1].split(',')

    # print('입력된 변수들 확인:', p, n, num)

    print(solution(p, n, num))