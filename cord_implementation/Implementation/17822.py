import sys
input = sys.stdin.readline
from collections import deque
n,m,t = map(int, input().split())
board = [deque(int(x) for x in input().split()) for _ in range(n)]
roll = [0]*t
for i in range(t):
    xi, di, ki = map(int, input().split())
    roll[i] = [xi, di, ki]

for x, d, k in roll:
    res = 0
    for i in range(n):
        res += sum(board[i])
        if (i+1)% x == 0:
            if d == 0:
                board[i].rotate(k)
            else:
                board[i].rotate(-k)
    if res != 0:
        delete = []
        for i in range(n):
            for j in range(m-1):
                if board[i][j] == board[i][j+1] and board[i][j] != 0 and board[i][j+1] != 0:
                    delete.append((i,j))
                    delete.append((i,j+1))
            if board[i][0] != 0 and board[i][-1] != 0 and board[i][0] == board[i][-1]:
                delete.append((i,0))
                delete.append((i,m-1))

        for j in range(m):
            for i in range(n-1):
                if board[i][j] != 0 and board[i+1][j] != 0 and board[i][j] == board[i+1][j]:
                    delete.append((i,j))
                    delete.append((i+1,j))

        delete = list(set(delete)) #중복 제거
        for i in range(len(delete)):
            y,x = delete[i]
            board[y][x] = 0

        if len(delete) == 0:
            average = 0
            cnt = 0
            for i in range(n):
                average += sum(board[i])
                cnt += board[i].count(0)

            ans = average // (n*m - cnt)

            for i in range(n):
                for j in range(m):
                    if board[i][j] != 0 and board[i][j] > ans:
                        board[i][j] -=1
                    elif board[i][j] != 0 and board[i][j] < ans:
                        board[i][j] += 1
    else:
        break

result = 0
for i in range(n):
    result += sum(board[i])
print(result)