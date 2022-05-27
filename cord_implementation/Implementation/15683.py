import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
copyBoard = board
# 4, 2, 4, 4, 1 4*2*4**8*4*1 = 65536
chk = [[False]*m for _ in range(n)]

direction = {
    1 : [[[-1,0]],[[1,0]],[[0,-1]],[[0,1]]],
    2 : [[[-1,0],[1,0]],[[0,-1],[0,1]]],
    3 : [[[-1,0],[0,-1]], [[-1,0],[0,1]], [[1,0],[0,-1]], [[1,0],[0,1]]],
    4 : [[[-1,0],[1,0],[0,-1]], [[-1,0],[1,0],[0,1]], [[-1,0],[0,-1],[0,1]],[[1,0],[0,-1],[0,1]]],
    5 : [[[-1,0],[1,0],[0,-1],[0,1]]]
}

def is_valid_coord(x,y):
    return 0 <= x < m and 0 <= y < n
def change(x,y,directon,copyBoard):
    for dir in direction:
        nx, ny = x, y
        while True:
            nx += dir
            ny += dir
            if not is_valid_coord(nx,ny) or copyBoard[ny][nx] == 6:
                break
            elif copyBoard[ny][nx] == 0:
                copyBoard[ny][nx] = '#'

def dfs(n):
    global copyBoard
    global res
    if n == len(cctv):
        cnt = 0
        for i in copyBoard:
            if i ==0:
                cnt += 1
        res = min(res, cnt)
        return

    a, b, c = cctv[n]
    for d in direction[c]:
        change(a,b,d,copyBoard)
        dfs(n+1)
        copyBoard = board
res = 64

cctv = []
for i in range(n):
    for j in range(m):
        if board[i][j] != 6 and board[i][j] != 0:
            cctv.append([i,j,board[i][j]])

dfs(0)
print(res)