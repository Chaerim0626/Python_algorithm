import sys
input = sys.stdin.readline
res = 64
cctvCnt = 0
cctv = []
n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().strip().split())))
# 4, 2, 4, 4, 1 4*2*4**8*4*1 = 65536
chk = [[False]*m for _ in range(n)]

direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def is_valid_coord(y,x):
    return 0 <= x < m and 0 <= y < n

def change(x,y,direction,copyBoard):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if is_valid_coord(ny,nx) and copyBoard[ny][nx] != 6:
                if copyBoard[ny][nx] == 0:
                    copyBoard[ny][nx] = '#'
            else:
                break

def dfs(board,cnt):
    copyBoard = [i[:] for i in board] #deepcopy대신 슬라이싱 쓰자
    global res
    if cnt == cctvCnt:
        tmp = 0
        for i in range(n):
            for j in range(m):
                if copyBoard[i][j] == 0:
                    tmp += 1
        res = min(res, tmp)
        return
    y, x, c = cctv[cnt]
    for i in direction[c]:
        change(x,y,i,copyBoard)
        dfs(copyBoard,cnt+1)
        copyBoard = [i[:] for i in board]

for i in range(n):
    for j in range(m):
        if board[i][j] != 6 and board[i][j] != 0:
            cctv.append([i,j,board[i][j]]) #cctv위치 저장
            cctvCnt += 1

dfs(board,0)
print(res)