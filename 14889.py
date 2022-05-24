import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input().strip())
s = [list(map(int, input().split())) for _ in range(n)]

it = list(combinations(range(1, n+1), n//2))

min_gap = int(1e9)

for i in range(len(it)//2):
    start_team = 0
    link_team = 0

    # print(it[i], it[-i-1])
    # print(f'\n팀 편성: {it[i]}, {it[-i-1]}')

    for steam in combinations(it[i], 2):
        # print('s_team:', steam)
        start_team += s[steam[0]-1][steam[1]-1]
        start_team += s[steam[1]-1][steam[0]-1]


    for lteam in combinations(it[-i-1], 2):
        # print('l_team:', lteam)
        link_team += s[lteam[0]-1][lteam[1]-1]
        link_team += s[lteam[1]-1][lteam[0]-1]
    
    gap = abs(start_team - link_team)
    min_gap = min(min_gap, gap)


print(min_gap)