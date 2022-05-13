N = int(input())

arr = list(map(int, input().split()))

dp = [1] * (N+1)

for i in range(2,N+1):
    for j in range(2,i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))