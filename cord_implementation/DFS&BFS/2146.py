import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

chk = [[False]*n for _ in range(n)]
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def is_valid_coord(y,x):
    return 0 <= x < n and 0 <= y < n

def land(sy,sx):
    global a
    q = deque()

    chk[sy][sx] = True
    board[sy][sx] = a
    q.append((sy,sx))

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny,nx) and not chk[ny][nx] and board[ny][nx] == 1:
                chk[ny][nx] = True
                board[ny][nx] = a
                q.append((ny,nx))


def bfs(num):

    global res

    res = sys.maxsize
    dis = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j] == num:
                q.append((i, j))
                dis[i][j] = 0

    while q:
        y,x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if is_valid_coord(ny,nx) and board[ny][nx] > 0 and board[ny][nx] != num:
                res = min(res, dis[y][x])
                return
            if is_valid_coord(ny,nx) and dis[ny][nx] == -1 and board[ny][nx] == 0:
                dis[ny][nx] = dis[y][x] + 1
                q.append((ny,nx))

a = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not chk[i][j]:
            land(i,j)
            a += 1

for i in range(1,a):
    bfs(i)

print(res)
