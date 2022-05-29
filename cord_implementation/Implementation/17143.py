import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[0]*C for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = [s,d,z]

for i in range(C):
    #