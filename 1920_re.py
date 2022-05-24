def binary_search(data, target, start=0, end=None):
    if end == None:
        end = len(data) - 1
    if start > end:
        return 0

    mid = (start + end) // 2

    if target == data[mid]:
        return 1
    elif target < data[mid]:
        end = mid - 1
    elif data[mid] < target:
        start = mid + 1

    return binary_search(data, target, start, end)


n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))


for num in m_list:
    print(binary_search(n_list, num))