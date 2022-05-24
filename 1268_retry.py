from sys import stdin

input = stdin.readline

n = int(input().strip())

students = []
dist = [[set() for _ in range(10)] for _ in range(5)]
counts = []

# 정보를 받으면서 바로 바로 dist내부의 set에 저장
for s in range(n):
    student = list(map(int, input().split()))
    students.append(student)
    # 학년 반복
    for c in range(5):
        dist[c][student[c]].add(s)

for s in range(n):
    count = set()
    for c in range(5):
        count |= dist[c][students[s][c]]

    counts.append(len(count))

print(dist)
# [
# [set(), set(), {0}, set(), {1}, {2}, {3}, set(), {4}, set()],
# [set(), {1}, set(), {0}, {4}, {2, 3}, set(), set(), set(), set()],
# [set(), {0}, {2, 3, 4}, set(), set(), set(), set(), set(), set(), {1}],
# [set(), set(), {4}, set(), {2}, set(), {1, 3}, {0}, set(), set()],
# [set(), set(), {4}, {0}, {2}, set(), set(), {3}, {1}, set()]
# ]

# print(counts.index(max(counts))+1)