from sys import stdin
from collections import Counter

n = int(stdin.readline())
cards = stdin.readline().split()

m = int(stdin.readline())
numbers = stdin.readline().split()

c = Counter(cards)
# print(' '.join('f{c[num]}' if num in cards else '0' for num in numbers))

for num in numbers:
    if num in c:
        print(c[num], end=' ')
    else:
        print(0, end=' ')