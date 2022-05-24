from sys import stdin

def compare(sample, book):
    for b in book:
        count = 0
        for i in range(6):
            if b[i] == sample[i]:
                count += 1
        
        if count >= 5:
            return b
    
    return False
            

code_book = {'000000': 'A', '001111': 'B', '010011': 'C', '011100': 'D', '100110': 'E', '101001': 'F', '110101': 'G', '111010': 'H'}

input = stdin.readline

n = int(input().strip())

raw_code = input().strip()
answer = ''
start, end = 0, 6

for i in range(n):
    code = raw_code[start:end]
    if code in code_book:
        answer += code_book[code]
    else:
        if compare(code, code_book) is False:
            answer = i + 1
            break
        else:
            answer += code_book[compare(code, code_book)]
    start, end = start + 6, end + 6
            
print(answer)