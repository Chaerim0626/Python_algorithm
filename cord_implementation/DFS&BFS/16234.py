import sys
input = sys.stdin.readline
#메모리 초과가 뜰 때 재귀 횟수를 줄여주자
sys.setrecursionlimit(10**5)

N, L, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
dx = (1,0,-1,0)
dy = (0,1,0,-1)
cntMove= 0

def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < N

def dfs(y,x,chk, arr):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny,nx) and not chk[ny][nx]:
            if L <= abs(arr[y][x] - arr[ny][nx]) <= R:
                chk[ny][nx] = True
                p.append([ny, nx])
                dfs(ny,nx,chk,arr)
    return p

while True:
    chk = [[False] * N for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            p = [[i,j]]
            if not chk[i][j]:
                chk[i][j] = True
                p = dfs(i,j,chk,arr)
                if len(p) > 1:
                    flag = False
                    sumArr = 0
                    for y, x in p:
                        sumArr += arr[y][x]
                    avg = sumArr//len(p)
                    for y, x in p:
                        arr[y][x] = avg
    if flag:
        break
    cntMove += 1
print(cntMove)








