import sys

n = int(sys.stdin.readline())

dictionary = []

[dictionary.append(sys.stdin.readline().strip()) for _ in range(n)]

set_dict = set(dictionary)
dictionary = list(set_dict)
dictionary.sort()
dictionary.sort(key=len)

for word in dictionary:
    print(word)