import sys
input = sys.stdin.readline

dx = [1,0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = [[0]*101 for _ in range(101)]

def is_valid_coord(y,x):
    return 0 <= x <= 100 and 0 <= y <= 100
for i in range(n):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1

    turn = [d]
    for j in range(g):
        for k in range(len(turn)-1,-1,-1):#거꾸로 turn끝값부터
            turn.append( (turn[k]+1) % 4) #배열에 추가

    for j in range(len(turn)):
        x += dx[turn[j]]
        y += dy[turn[j]]
        if not is_valid_coord(y,x):
            continue
        board[y][x] = 1

cnt =0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            cnt += 1
print(cnt)