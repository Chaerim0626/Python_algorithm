import sys
input = sys.stdin.readline
from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

sharkSize = 2
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            y,x = i, j

def is_valid_coord(y,x):
    return 0 <= x < n and 0 <= y < n

def bfs(sy,sx,sharkSize):
    d = [[0]*n for _ in range(n)]
    chk = [[False]*n for _ in range(n)]
    q = deque()
    q.append([sy,sx])
    chk[sy][sx] = True
    fish = []
    while q:
        cy, cx = q.popleft()
        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]
            if is_valid_coord(ny,nx) and not chk[ny][nx]:
                if board[ny][nx] <= sharkSize:
                    q.append([ny,nx])
                    chk[ny][nx] = True
                    d[ny][nx] = d[cy][cx] + 1
                    if board[ny][nx] < sharkSize and board[ny][nx] != 0:
                        fish.append([ny,nx,d[ny][nx]])

    fish.sort(key=lambda i: (-i[2], -i[0],-i[1]))
    return fish
time = 0
eatCnt = 0
while True:
    cntfish = bfs(y,x,sharkSize)
    board[y][x] = 0
    if not cntfish:
        break
    ny, nx, d = cntfish.pop()
    time += d
    board[ny][nx] = 0

    x, y = nx, ny
    eatCnt +=1
    if eatCnt == sharkSize:
        sharkSize += 1
        eatCnt = 0

print(time)




