from sys import stdin
from math import gcd

input = stdin.readline

n = int(input().strip())
a = int(input().strip())

interval = []

for i in range(n-1):
    num = int(input().strip())
    interval.append(num - a)
    a = num
    
g = interval[0]

for j in range(1, len(interval)):
    g = gcd(g, interval[j])

count = 0

for i in interval:
    count += i // g - 1

print(count)