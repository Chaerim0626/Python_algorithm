import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.reverse()
ans = 0

for i in range(n):
    ans += k //coins[i]
    k = k % coins[i]
    if k == 0:
        break
print(ans)