from collections import deque
import sys

n = int(sys.stdin.readline())

q = deque()

for _ in range(n):
    user_input = list(sys.stdin.readline().split())
    order = user_input[0]

    if order == 'push':
        q.append(user_input[1])
    elif order == 'pop':
        if bool(q):
            print(q.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if bool(q) is False:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if bool(q):
            print(q[0])
        else:
            print(-1)
    elif order == 'back':
        if bool(q):
            print(q[-1])
        else:
            print(-1)
            
