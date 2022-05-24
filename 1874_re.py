from sys import stdin

n = int(stdin.readline().strip())

count = 1
push_or_pop = []
flag = True
stack = []

for _ in range(n):
    num = int(stdin.readline().strip())

    while count <= num:
        stack.append(count)
        push_or_pop.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        push_or_pop.append('-')
    else:
        flag = False
        break


if flag is False:
    print('NO')
else:
    for p_or_p in push_or_pop:
        print(p_or_p)