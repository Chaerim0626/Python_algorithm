import sys
input = sys.stdin.readline
board = []
for i in range(10):
    board.append(list(map(int, input().split())))

cntPaper = [0,0,0,0,0]
res = 26

def backtracking(x,y,cnt):
    global res

    if y > 9 :
        res = min(res, cnt)
        return
    if x > 9:
        backtracking(0,y+1,cnt)
        return
    if board[y][x] == 1:
        for i in range(5):
            if cntPaper[i] == 5:
                continue
            if x + i > 9 or y + i > 9:
                continue
            flag = False
            for j in range(y, y+i+1):
                for k in range(x, x+i+1):
                    if board[j][k] == 0:
                        flag = True
                        break
                if flag:
                    break

            if not flag:
                for j in range(y, y+i+1):
                    for k in range(x, x+i+1):
                        board[j][k] = 0

                cntPaper[i] +=1
                backtracking(x+i+1,y,cnt+1)
                cntPaper[i] -= 1

                for j in range(y, y+i+1):
                    for k in range(x, x+i+1):
                        board[j][k] = 1
    else:
        backtracking(x+1,y,cnt)

backtracking(0,0,0)
print(res) if res != 26 else print(-1)