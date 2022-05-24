n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
avg = 0

for score in scores:
    avg += (score/m*100)

print(avg/n)