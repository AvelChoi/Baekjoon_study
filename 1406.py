import sys

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []

m = int(sys.stdin.readline())

for _ in range(m):
    user_input = list(sys.stdin.readline().split())
    order = user_input[0]
    if order == 'L':
        if stack1:
            stack2.append(stack1.pop())
    
    elif order == 'D':
        if stack2:
            stack1.append(stack2.pop())

    elif order == 'B':
        if stack1:
            stack1.pop()

    else:
        stack1.append(user_input[1])


stack1.extend(reversed(stack2))
print(''.join(stack1))