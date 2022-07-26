N = int(input())

arr = list(map(int, input().split()))

dp = [1] * (N+1)

for i in range(1,N+1):
    for j in range(1,i):
        if arr[j-1] < arr[i-1]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))