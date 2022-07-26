import sys
input = sys.stdin.readline

arr = [[0]*14 for _ in range(15)]
for i in range(1,15):
    arr[0][i-1] = i
for i in range(1,15):
    arr[i][0] = 1
for i in range(1,15):
    for j in range(1,14):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(arr[k][n-1])