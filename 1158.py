n, k = map(int, input().split())

array = [i for i in range(1, n+1)]
num = 0
answer = []

for i in range(n):
    num += k-1
    if num >= len(array):
        num = num % len(array)
    
    answer.append(str(array.pop(num)))

print('<', ', '.join(answer), '>', sep='')