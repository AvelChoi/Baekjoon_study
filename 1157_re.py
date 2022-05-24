def freq(source):
    result = []
    reduce = list(set(source))
    
    for text in reduce:
        result.append(source.count(text))

    # if cnt_list.count(max(cnt_list)) > 1 :
    if result.count(max(result)) > 1:
        return '?'
    else:
        max_index = result.index(max(result))

    return reduce[max_index]


word = input().upper()
print(freq(word))

# testcase = ['Mississipi', 'zZa', 'z', 'baaa']

# for test in testcase:
#     print(freq(test))