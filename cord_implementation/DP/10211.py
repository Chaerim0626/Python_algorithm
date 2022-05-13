import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0]*(n+1)
    dp[0] = -1000
    arr = list(map(int, input().split()))
    dp[1] = arr[0]
    for i in range(2,n+1):
        dp[i] = max(arr[i-1], dp[i-1]+arr[i-1])
    print(max(dp))