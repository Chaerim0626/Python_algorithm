import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]
start = 1
end = max(lans)

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in lans:
        cnt += i // mid

    if cnt < n:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)

