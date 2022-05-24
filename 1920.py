# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

def binary_search(element, data, start=0, end=None):
    if end == None:
        end = len(data) - 1
    if start > end:
        return 0

    mid = (start + end) // 2
    
    if element == data[mid]:
        return 1
    elif element > data[mid]:
        start = mid + 1
    elif element < data[mid]:
        end = mid - 1

    return binary_search(element, data, start, end)
    


n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

for i in range(len(m_list)):
    print(binary_search(m_list[i], n_list))