from sys import stdin
from itertools import combinations

def lotto(data):
    k = data[0]
    s = data[1:]
    
    answer = combinations(s, 6)

    return answer

while True:
    numbers = list(map(int, stdin.readline().split()))
    if numbers == [0]:
        break
    else:
        lotto_nums = list(lotto(numbers))
        for l in lotto_nums:
            print(* l)
    
    print()
