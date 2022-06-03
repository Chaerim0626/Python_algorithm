import sys
import copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
dy = [1,0,-1,0]
dx = [0,1,0,-1]
for i in range(n):
    board.append(list(map(int, input().split())))

def is_valid_coord(y,x):
    return 0 <= x < m and 0 <= y < n

def disChk(sy,sx): #옆의 0체크해서 빙산 줄여주는 함수
    cnt = 0
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]

        if is_valid_coord(ny,nx) and checkBoard[ny][nx] == 0:
            cnt += 1
    return cnt

def cntIce(sy,sx):
    q = deque()
    q.append((sy,sx))
    chk[sy][sx] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_coord(ny,nx) and not chk[ny][nx] and board[ny][nx] != 0:
                chk[ny][nx] = True
                q.append((ny,nx))
def chkAll():
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                return False
    return True
year = 1
while True:
    chk = [[False] * m for _ in range(n)]
    piece = 0

    if chkAll():
        print(0)
        break

    checkBoard = [a[:] for a in board]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if checkBoard[i][j] != 0:
                board[i][j] = max(0,board[i][j] - disChk(i,j))

    for i in range(1,n-1):
        for j in range(1,m-1):
            if board[i][j] != 0 and not chk[i][j]:
                cntIce(i,j)
                piece += 1
    if piece > 1:
        print(year)
        break

    year += 1

