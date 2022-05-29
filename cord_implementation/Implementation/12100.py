import sys
input = sys.stdin.readline
import copy
sys.setrecursionlimit(10**5)

maxValue = 0
n= int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def move(direction):
    if direction == 0:
        for j in range(n):
            direction = 0
            for i in range(1,n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[direction][j] == 0:
                        board[direction][j] = tmp
                    elif board[direction][j] == tmp:
                        board[direction][j] = tmp*2
                        direction += 1
                    else:
                        direction += 1
                        board[direction][j] = tmp
    elif direction == 1:
        for j in range(n):
            direction = n-1
            for i in range(n-2,-1,-1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[direction][j] == 0:
                        board[direction][j] = tmp
                    elif board[direction][j] == tmp:
                        board[direction][j] = tmp*2
                        direction -= 1
                    else:
                        direction -= 1
                        board[direction][j] = tmp

    elif direction == 2: #우로 이동
        for i in range(n):
            direction = n-1
            for j in range(n-2,-1,-1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][direction] == 0:
                        board[i][direction] = tmp
                    elif board[i][direction] == tmp:
                        board[i][direction] = tmp*2
                        direction -= 1
                    else:
                        direction -= 1
                        board[i][direction] = tmp
    else:
        for i in range(n):
            direction = 0
            for j in range(1,n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][direction] == 0:
                        board[i][direction] = tmp
                    elif board[i][direction] == tmp:
                        board[i][direction] = tmp*2
                        direction += 1
                    else:
                        direction += 1
                        board[i][direction] = tmp

def dfs(cnt):
    global maxValue
    global board
    if cnt == 5:
        for i in range(n):
            maxValue = max(maxValue,max(board[i]))
        return
    a = copy.deepcopy(board)

    for i in range(4):
        move(i)
        dfs(cnt+1)
        board = copy.deepcopy(a)

dfs(0)
print(maxValue)