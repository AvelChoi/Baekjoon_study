from sys import stdin
from itertools import combinations

while 1:
    arr = input().split()

    if arr.pop(0) == '0':
        break

    for i in combinations(arr, 6):
        print(' '.join(i))
    
    print()