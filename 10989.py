import sys

n = int(sys.stdin.readline())

data = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    
    data[num] += 1
    

for i in range(10001):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)