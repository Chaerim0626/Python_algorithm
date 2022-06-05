import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def is_valid_coord(y,x):
    return 0 <= x < n and 0 <= y < n

#오.. chk배열 빼주니까 시간초과 안남
def dfs(sy,sx):
    if dp[sy][sx]: return dp[sy][sx]
    dp[sy][sx] = 1

    for k in range(4):
        ny = sy + dy[k]
        nx = sx + dx[k]
        if is_valid_coord(ny,nx) and board[ny][nx] > board[sy][sx]:
            dp[sy][sx] = max(dp[sy][sx], dfs(ny,nx) + 1 )
            #현재 거리 값이나, 진행 거리값 중 큰 값
    return dp[sy][sx]

n = int(input())
board = []
dy = [1,0,-1,0]
dx = [0,1,0,-1]
res = 0
dp = [[0] * n for _ in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        res = max(res,dfs(i,j))
print(res)