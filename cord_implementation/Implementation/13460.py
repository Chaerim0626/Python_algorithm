import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(str,input().strip())))

dy = [1,0,-1,0]
dx = [0,1,0,-1]
dq = deque()
chk =[[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n): #구슬 위치 저장
    for j in range(m):
        if board[i][j] == 'R':
            ry, rx = i, j
        elif board[i][j] == 'B':
            by, bx = i,j

def move(y,x,dy,dx):
    cnt = 0
    while board[y+dy][x+dx] != "#" and board[y][x] != 'O':
        #다음좌표가 벽이 아니고 현재좌표가 구멍도 아닐동안
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

def bfs(ry,rx,by,bx):
    chk[ry][rx][by][bx] = True
    dq.append([ry,rx,by,bx,1])
    while dq:
        print(dq)
        ry, rx, by, bx, d = dq.popleft()

        if d > 10:
            print(-1)
            return
        for i in range(4):
            nry,nrx,rcnt = move(ry,rx,dy[i],dx[i])
            nby,nbx,bcnt = move(by,bx,dy[i],dx[i])
            print(nry,nrx,nby,nbx)
            if board[nby][nbx] != 'O': #파란 구슬 아직 안들어감
                if board[nry][nrx] == 'O': #빨간구슬은 들어감
                    print(d)
                    return
                if nry == nby and nrx == nbx: #파랑 빨강 좌표가 같음
                    if rcnt > bcnt : #빨강이 더 멀리 있었다면 전 좌표에
                        nry -= dy[i]
                        nrx -= dx[i]
                    else: #파랑이 더 멀리 있었다면 파랑을 전 좌표에
                        nby -= dy[i]
                        nbx -= dx[i]
                if not chk[nry][nrx][nby][nbx]:
                    chk[nry][nrx][nby][nbx] = True
                    dq.append([nry,nrx,nby,nbx,d+1])
    print(-1)
bfs(ry,rx,by,bx)