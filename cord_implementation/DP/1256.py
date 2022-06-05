import sys
input = sys.stdin.readline
from itertools import permutations

N, M, K = map(int, input().split())
dp = [[1]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
#a N개로 만들 수 있는 경우의수, z M개로 만들 수 있는 경우의 수
if dp[N][M] < K:
    print(-1)
else:
    word = ""
    while True:
        if N == 0:
            word += "z"*M
            break
        elif M == 0:
            word += "a"*N
            break
        flag = dp[N-1][M]
        if K <= flag:
            word += "a"
            N -= 1
        else:
            word += "z"
            M -= 1
            K -= flag
    print(word)





