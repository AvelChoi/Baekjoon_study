from sys import stdin
from collections import deque

def print_que(m, p):
    count = 0
    
    while p:
        maxx = max(p)
        front = p.popleft()
        m -= 1

        if maxx == front:
            count += 1
            if m < 0:
                return count
        
        else:
            p.append(front)

            if m < 0:
                m = len(p) - 1
            

testcase = int(stdin.readline().strip())

for _ in range(testcase):
    n, m = map(int, stdin.readline().split())
    priority = deque(list(map(int, stdin.readline().split())))
    print(print_que(m, priority))