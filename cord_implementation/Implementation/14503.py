import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = []
chk = [[False]*m for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1] #북 동 남 서

for i in range(n):
    board.append(list(map(int, input().split())))
chk[r][c] = True #시작위치 청소
cnt = 1

def turnLeft():
    global d
    d -=1
    if d == -1:
        d = 3
turnCnt = 0
while True:
    turnLeft()
    nx = c +dx[d]
    ny = r +dy[d]

    if board[ny][nx] == 0 and chk[ny][nx] == False:
        chk[ny][nx] = True
        cnt += 1
        r, c = ny, nx
        turnCnt = 0

    else:
        turnCnt += 1

    if turnCnt == 4:
        nx = c - dx[d]
        ny = r - dy[d]
        if board[ny][nx] == 1:
            break
        else:
            r, c = ny, nx
        turnCnt = 0

print(cnt)