# 기존: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이번: (3D) 위 아래, (2D) 상하좌우


# graph[i][j][k]

# for i in range(h):
# for j in range(n):
# for k in range(m):
# for문 순서 변경? 혹은 순서 추가?




'''
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
# 2판이 있는 상태, 아래로 가려면?
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
'''

'''
[
[
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]],
[
    [0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0]]
]
'''
