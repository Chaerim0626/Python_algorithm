import sys
input = sys.stdin.readline
from collections import deque
n,m,K = map(int, input().split())
board = []
dy = [1,0,-1,0]
dx = [0,1,0,-1]

for i in range(n):
    board.append(list(map(int, input().split())))
q = deque()
def is_valid_coord(y,x):
    return 0 <= x < m and 0 <= y < n

def cnt(num):
    chk = [[False] * m for _ in range(n)]
    res = 0
    if n == 1 or m == 1:
        for i in range(n):
            for j in range(m):
                if board[i][j] <= num:
                    res += 1
        return res
 #꼭짓점 4개 값 탐방
    if board[0][0] <= num:
        chk[0][0] = True
        q.append((0,0))
    if board[0][m-1] <= num:
        chk[0][m-1] = True
        q.append((0, m-1))
    if board[n-1][0] <= num:
        chk[n-1][0] = True
        q.append((n-1, 0))
    if board[n-1][m-1] <= num:
        chk[n-1][m-1] = True
        q.append((n-1, m-1))


    #밖에꺼 3줄 탐방 (꼭짓점 제외)
    for i in range(1,n-1):
        if board[i][0] <= num:
            chk[i][0] = True
            q.append((i,0))
        if board[i][m-1] <= num:
            chk[i][m-1] = True
            q.append((i,m-1))
    for j in range(1,m-1):
        if board[0][j] <= num:
            chk[0][j] = True
            q.append((0,j))

    while q:
        res += 1
        #가장자리쪽 먼저 뺌
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if not is_valid_coord(ny,nx) or chk[ny][nx] or board[ny][nx] > num:
                continue

            if is_valid_coord(ny,nx) and not chk[ny][nx] and board[ny][nx] <= num:
                #가장자리 한개부터 이미 큐에 넣은거 아니면 추가
                chk[ny][nx] = True
                q.append((ny,nx))

    return res

start = 0
end = 1000000

while start != end:
    mid = (start+end)//2
    if cnt(mid) < K:
        start = mid + 1
    else:
        end = mid
print(start)