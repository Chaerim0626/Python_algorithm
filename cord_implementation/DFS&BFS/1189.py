import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
R, C, K = map(int, input().split())
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False]*C for _ in range(R)]

def is_valid_coord(y, x):
     return 0 <= y < R and 0 <= x < C
dic = {}
def dfs(y, x, cnt):
    if x == C-1 and y == 0 :
        if cnt in dic:
            dic[cnt] += 1
        else:
            dic[cnt] = 1

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny,nx) and not chk[ny][nx] and board[ny][nx] != 'T':
            dfs(ny,nx,cnt+1)

board = [input().strip() for _ in range(R)]
dfs(R-1,0,1)
print(dic[K] if K in dic else 0)
