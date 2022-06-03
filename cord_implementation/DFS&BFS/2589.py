import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
dy = [1,0,-1,0]
dx = [0,1,0,-1]

d = []
q = deque()

def is_valid_coord(y,x):
    return 0 <= y < n and 0 <= x < m

def bfs(sy,sx):
    chk = [[False] * m for _ in range(n)]
    q.append([i,j,0])
    chk[i][j] = True
    while q:
        y,x,depth = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_valid_coord(ny,nx) and not chk[ny][nx] and board[ny][nx] == 'L':
                chk[ny][nx] = True #방문체크 까먹지 말 것
                q.append([ny,nx,depth+1])
    d.append(depth)
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            bfs(i,j)
print(max(d))

