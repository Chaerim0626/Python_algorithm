import sys
input = sys.stdin.readline

n=int(input())
dp = [0]*10
dp[1] = 9
for i in range(2,10):
    dp[i] = dp[i-1] + (10**(i-1))*9*i

m = len(str(n))

if m == 1:
    print(n)
else:
    res = dp[m-1] + (n - (10**(m-1)) + 1 )*m
    print(res)