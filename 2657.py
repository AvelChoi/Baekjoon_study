def solution(r, s):
    answer = ''
    for text in s:
        answer += text * r
    return answer

for i in range(int(input())):
    r, s = input().split()
    print(solution(int(r), s))