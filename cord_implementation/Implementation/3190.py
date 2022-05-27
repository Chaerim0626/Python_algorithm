import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())
dir = {}
dq = deque()
board = [[0]*n for _ in range(n)]

for i in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 2

l = int(input())
for i in range(l):
    x, c = map(str, input().split())
    dir[x] = c

nx, ny = 0,0
direction = 0

def is_valid_coord(cx,cy) :
    return 0 <= cx < n and 0 <= cy < n

dx = [1, 0,-1, 0] #우 하 좌 상
dy = [0, 1, 0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def turn_right():
    global direction
    direction +=1
    if direction == 4:
        direction = 0

cnt=0
dq.append([0,0])
while True:
    cnt += 1
    nx += dx[direction]
    ny += dy[direction]



    if not is_valid_coord(nx,ny) or [ny, nx] in dq:
        break

    if str(cnt) in dir.keys():
        if dir[str(cnt)] == 'L':
            turn_left()
        else:
            turn_right()

    if board[ny][nx] == 2:
        board[ny][nx] = 0
        dq.append([ny, nx])

    elif board[ny][nx] == 0:
        dq.append([ny,nx])
        dq.popleft()

print(cnt)
