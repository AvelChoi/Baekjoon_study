n = int(input())

# 모든 단위를 초로 환산
buttons = [300, 60, 10]
button_push = []
    
for b in buttons:
    button_push.append(n // b)
    n = n % b

if n != 0:
    print(-1)
else:
    print(* button_push)