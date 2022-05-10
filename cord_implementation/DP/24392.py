import sys
input = sys.stdin.readline
arr = []
n,m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input().strip().split())))

for i in range(m):
    if arr[n-1][i] == 1:
        dp[n-1][i] = 1


for i in range(n-2,-1,-1):
    for j in range(m):
        if arr[i][j] == 1:
            dp[i][j] = dp[i+1][j-1] + dp[i+1][j] + dp[i+1][j+1]

print(dp)
res = sum(dp[0])
print(res%1000000007)
