from sys import stdin as st

def vps(valid):
    if valid[0] != '(' or valid[-1] != ')':
        return 'NO'

    open = 0
    closed = 0
        
    for v in valid:
        # print('for문 도는 중' ,'open:', open, ', closed:', closed)
        if v == '(':
            open += 1
        elif v == ')' and open > 0:
            closed += 1
            open -= 1
        else:
            return 'NO'
    
    # print('end - ' ,'open:', open, ', closed:', closed)

    if open != 0:
        return 'NO'
    else:
        return 'YES'


n = int(st.readline())

for _ in range(n):
    print(vps(st.readline().strip()))
