import sys

# n = int(sys.stdin.readline())
# n_list = sorted(list(map(int, sys.stdin.readline().split())))

# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))

# print('n:', n, ', n_list:', n_list, ', m:', m, ', m_list:', m_list)

n = 5
n_list = [-10, 2, 3, 6, 10]
m = 8
m_list = [10, 9, -5, 2, 3, 4, 5, -10]


def binary_search(target, data, start=0, end=None):
    if end == None:
        end = len(data)
    if start > end:
        return 0

    mid = (start + end) // 2
    
    if target == data[mid]:
        return 1
    elif target < data[mid]:
        end = mid - 1
    elif data[mid] < target:
        start = mid + 1

    return binary_search(target, data, start, end)


for m_num in m_list:
    print(binary_search(m_num, n_list), end=' ')