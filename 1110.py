from collections import deque
n = int(input())

def solution(num):
    q = deque([n])
    count = 0
    while q:
        count += 1
        num = q.popleft()

        if int(num) >= 10:
            a = str(num)[0]
            b = str(num)[-1]
            step1 = int(a) + int(b)
        else:
            step1 = num


        step2 = str(num)[-1] + str(step1)[-1]
        # print(int(step2))
        
        if int(step2) == n:
            return count
        else:
            q.append(step2)


print(solution(n))