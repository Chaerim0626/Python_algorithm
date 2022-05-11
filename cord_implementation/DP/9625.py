import sys
input = sys.stdin.readline
k = int(input())

dp = [0, 0]*(k+1)
dp[1] = [0,1]
for i in range(2,k+1):
    dp[i] = [dp[i-1][1], dp[i-1][0]+dp[i-1][1]]

print(*dp[k])

