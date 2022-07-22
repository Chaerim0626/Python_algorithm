import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

arr.sort()

res = 0
cnt = 0

for i in arr:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
print(res)