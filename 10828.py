import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push':
        value = word[1]
        stack.append(value)
    
    elif order == 'pop':
        if bool(stack) is False:
            print(-1)
        else:
            print(stack.pop())
    
    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if bool(stack) is False:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if bool(stack) is False:
            print(-1)
        else:
            print(stack[-1])
            