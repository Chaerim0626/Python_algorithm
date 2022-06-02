import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[0]*C for _ in range(R)]
sharkSize = 0

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = [s, d, z]

sharkSize = 0 #잡은 상어 크기

def move():
    global board
    newBoard = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:
                ny, nx, nd = getLoc(i,j,board[i][j][0], board[i][j][1])
                if newBoard[ny][nx]:
                    newBoard[ny][nx] = max(newBoard[ny][nx], (board[i][j][0], nd, board[i][j][2]),key=lambda x: x[2])
                else:
                    newBoard[ny][nx] = [board[i][j][0],nd,board[i][j][2]]
    board = newBoard

def getLoc(i, j, s, dir):

    if dir == 1 or dir == 2:
        c = R * 2 - 2
        if dir == 1:
            s += 2 * (R - 1) - i
        else:
            s += i

        s %= c
        if s >= R:
            return [2 * R - 2 - s, j, 1]
        return [s, j, 2]

    else:
        c = C * 2 - 2
        if dir == 4:
            s += 2 * (C - 1) - j
        else:
            s += j

        s %= c
        if s >= C:
            return [i, 2 * C - 2 - s, 4]
        return [i, s, 3]


def getShark(j):
    global sharkSize
    for i in range(R):
        if board[i][j] != 0:
            s = board[i][j][2]
            board[i][j] = 0
            sharkSize += s
            break
        else:
            sharkSize += 0


for i in range(C):
    getShark(i)
    move()

print(sharkSize)