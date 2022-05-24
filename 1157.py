def freq(source):
    result = []
    source = source.upper()
    reduce = set(source)
    
    for text in reduce:
        result.append((text, source.count(text)))

    result.sort(key=lambda x: x[1], reverse=True)
    # print(max(result, key=lambda x: x[1]))
    
    if len(result) > 1 and result[0][1] == result[1][1]:
        return '?'

    return result[0][0]


# word = input().split()
# print(freq(word))

testcase = ['Mississipi', 'zZa', 'z', 'baaa']

for test in testcase:
    print(freq(test))