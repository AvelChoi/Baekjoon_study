def ROT13(source):
    answer = ''
    for t in source:
        if 'a' <= t and t <= 'z':
            x = ord(t) + 13
            if x > 122:
                x -= 26
            answer += chr(x)
        
        elif 'A' <= t and t <= 'Z':
            x = ord(t) + 13
            if x > 90:
                x -= 26
            answer += chr(x)
        
        else:
            answer += t

    return answer

print(ROT13(input()))

# testcase = ['Baekjoon Online Judge', 'One is 1', 'Onrxwbba Bayvar Whqtr', 'Bar vf 1']
# for test in testcase:
#     print(ROT13(test))



# ord()를 이용, az, AZ의 아스키코드를 알아내야 한다
# a = 97, z = 122
# A = 65, z = 90

# ord('O') = 79
# 79 + 13 = 92
# 92 - 26 = 66, chr(66) = 'B'

# 25로 빼주면 Onrxwccb Cbyvbr Wiqtr
# 올바른 답은 O가 B로 변환되어야 함