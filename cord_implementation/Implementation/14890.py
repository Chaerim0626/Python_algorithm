import sys
input = sys.stdin.readline

n, l = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def check(line):
    for i in range(n-1):
        if abs(line[i] - line[i+1]) > 1:
            return False
        if line[i] > line[i+1]: #하락세는 i+1부터 l번 검사
            for j in range(l):
                if i + j+1 >= n or line[i+1] != line[i+j+1] or arr[i+j+1]:
                    return False
                if line[i+1] == line[i+j+1]:
                    arr[i+j+1] = True
        elif line[i] < line[i+1]: #상승세는 i부터 l번 검사
            for j in range(l):
                if i-j < 0 or line[i] != line[i-j] or arr[i-j]:
                    return False
                if line[i] == line[i-j]:
                    arr[i-j] = True
    return True

row = 0
for i in range(n):
    arr = [False]*n
    if check([board[i][j] for j in range(n)]):
        row += 1

col = 0
for j in range(n):
    arr = [False]*n
    if check([board[i][j] for i in range(n)]):
        col +=1

print(row+col)