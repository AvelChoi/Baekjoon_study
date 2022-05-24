from sys import stdin

def check_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num * 0.5) + 1):
            if num % i == 0:
                return False
        return True

n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
count = 0

for num in numbers:
    if check_prime(num):
        count += 1

print(count)