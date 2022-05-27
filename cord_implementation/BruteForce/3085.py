import sys
input = sys.stdin.readline
n = int(input())
row, col = 0, 0
candy = [list(map(str, input().strip())) for _ in range(n)]

#오른쪽, 아래쪽만 바꿔보면 됨
def rowCnt():
    global row
    for i in range(n):
        maxValue1 = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                maxValue1 += 1
                row = max(maxValue1, row)
            else:
                maxValue1 = 1
def colCnt():
    global col
    for i in range(n-1):
        maxValue2 = 1
        for j in range(n-1):
            if candy[j][i] == candy[j+1][i]:
                maxValue2 += 1
                col = max(maxValue2, col)
            else:
                maxValue2 = 1

for i in range(n):
    for j in range(n-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            rowCnt()
            colCnt()
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if candy[j][i] != candy[j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            rowCnt()
            colCnt()
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]

print(max(row,col))