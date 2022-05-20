import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = [list(map(int,list(input().strip()))) for _ in range(n)]
B = [list(map(int,list(input().strip()))) for _ in range(n)]

def rever(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
           A[i][j] = 1 - A[i][j]
cnt=0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            rever(i,j)
            cnt += 1

def check():
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False
    return True

if check():
    print(cnt)
else:
    print(-1)