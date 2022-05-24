m, n = map(int, input().split())

def check_prime(num):
    if num == 1:
        return False
    else:
        # num * 0.5 == num의 제곱근
        # 제곱근을 함수를 이용해 구하려면 import math 필요
        for i in range(2, int(num*0.5) + 1):
            if num % i == 0:
                return False
        return True

for i in range(m, n+1):
    if check_prime(i):
        print(i)

'''
풀이출처: https://imdona.tistory.com/m/25
'''