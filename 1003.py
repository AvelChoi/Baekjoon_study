count0 = [1, 0]
count1 = [0, 1]

test_case = int(input())

for i in range(test_case):
    test = int(input())

    if test == 0:
        print('1 0')
    elif test == 1:
        print('0 1')
    else:
        for j in range(2, test+1):
            count0.append(count0[j-1] + count0[j-2])
            count1.append(count1[j-1] + count1[j-2])
        print(f'{count0.pop()} {count1.pop()}')
        count0 = [1, 0]
        count1 = [0, 1]