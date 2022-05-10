import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m= map(int, input().strip().split())
    dp = [[0] *(m+1) for _ in range(m+1)]
    dp[0][0] = dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2,m+1):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print(dp[m][n])
