import sys
input = sys.stdin.readline
n= int(input())

dp = [0]*(n+1)
dp[2] = 3
for i in range(4,n+1,2):
    dp[i] = dp[i-2]+i
print(dp[n])