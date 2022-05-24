import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

# print('n:', n, ', n_list:', n_list, ', m:', m, ', m_list:', m_list)

# n = 5
# n_list = [6, 3, 2, 10, -10]
# m = 8
# m_list = [10, 9, -5, 2, 3, 4, 5, -10]

dict1 = {m_list[i]: 0 for i in range(m)}

for n_num in n_list:
    if n_num in dict1.keys():
        dict1[n_num] += 1

print(' '.join(map(str, list(dict1.values()))))