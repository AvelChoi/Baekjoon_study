def Rev(source):
    source = str(source)[::-1]
    return int(source)

x, y = map(int, input().split())

print((Rev(Rev(x) + Rev(y))))

# testcase = [[123, 100], [111, 111], [5, 5], [1000, 1], [456, 789]]

# for test in testcase:
#     print(Rev(Rev(test[0]) + Rev(test[1])))