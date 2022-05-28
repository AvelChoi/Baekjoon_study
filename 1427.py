import sys

n = sys.stdin.readline().strip()

n_list = sorted([int(i) for i in n], reverse=True)

n_str = [str(i) for i in n_list]

print(''.join(n_str))