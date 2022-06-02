import sys
input = sys.stdin.readline
n = 1
dp = [[0]*31 for _ in range(31)]

for i in range(1,31):
    dp[0][i] = 1 #반절짜리만 남았을때

for i in range(1,31):
    for j in range(30):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        else: #반절짜리 + 완전한거 한개 먹었을때
            dp[i][j] = dp[i][j-1] + dp [i-1][j+1]

while True:
    n = int(input())
    if n ==0:
        break
    print(dp[n][0])
