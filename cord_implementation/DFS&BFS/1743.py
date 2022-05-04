import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M,K = map(int, input().split())
dy = (0, 1, 0, -1) #우 상 좌 하
dx = (1, 0, -1, 0)

def is_vaild_coord(y, x):
    return 0 <= y < N and 0 <= x < M
board = [[0]*M for _ in range(N)]
chk = [[False]*M for _ in range(N)]
for _ in range(K):
     r, c = map(int, input().split())
     board[r-1][c-1] = 1

def dfs(y,x,cnt):
      for i in range(4):
          ny = y + dy[i]
          nx = x + dx[i]
          if is_vaild_coord(ny,nx) and not chk[ny][nx] and board[ny][nx]==1:
            chk[ny][nx] = True
            cnt = dfs(ny,nx,cnt+1)
      return cnt
res = []
for i in range(N):
       for j in range(M):
           if board[i][j] ==1:
              chk[i][j] = True
              res.append(dfs(i,j,1))
print(max(res))
