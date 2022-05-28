# https://kyoung-jnn.tistory.com/88

from sys import stdin

input = stdin.readline

t = int(input().strip())

Flag = True

for _ in range(t):
    n = int(input().strip())
    phone_book = sorted([input().strip() for _ in range(n)])

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            print("NO")
            Flag = False
            break

    if Flag:
        print("YES")
    Flag = True
