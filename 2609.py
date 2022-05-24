x, y = map(int, input().split())

gcd = 1 # 최대공약수
lcm = 1 # 최소공배수

i = 2

while i < 10000:
    if x % i == 0 and y % i == 0:
        x = x // i
        y = y // i

        gcd *= i
        lcm *= i

    else:
        i += 1
        continue

print(gcd)
print(lcm * x * y)