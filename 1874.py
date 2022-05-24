from sys import stdin

count = 1
flag = True
stack = []
calculating = []

n = int(stdin.readline().strip())

for i in range(n):
    # 입력을 받는 즉시 값을 비교
    num = int(stdin.readline().strip())
    
    # 입력 받은 수가 count보다 클 동안 반복
    while count <= num:
        stack.append(count)
        calculating.append('+')
        count += 1

    # 만약 스택 맨 앞에 있는 수가 입력 받은 숫자와 일치한다면
    # 해당 숫자를 pop 처리, - 부호를 op에 추가
    if stack[-1] == num:
        stack.pop()
        calculating.append('-')
    # 아니라면 일치하는 숫자가 없다는 뜻이므로 NO를 출력하기 위해 temp = False
    else:
        flag = False
        break


if flag == False:
    print('NO')
else:
    for i in calculating:
        print(i)