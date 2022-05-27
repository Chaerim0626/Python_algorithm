import sys
input = sys.stdin.readline

n,m,x,y,k= map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
direction = list(map(int, input().split()))

dice = [0,0,0,0,0,0]
def turn_dir(dir):
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

def move(dir):
    if dir == 1:
        return [0,1]
    elif dir == 2:
        return [0,-1]
    elif dir == 3:
        return [-1,0]
    else:
        return [1,0]

for i in direction:
    d = move(i)
    if 0 <= x + d[0] < n and 0 <= y + d[1] < m:
        x += d[0]
        y += d[1]
        turn_dir(i)
        if board[x][y] != 0:
            dice[5] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[5]
        print(dice[0])
