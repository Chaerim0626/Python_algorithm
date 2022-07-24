import sys
input = sys.stdin.readline

n = int(input())
card = sorted(list(map(int,input().split())))
m = int(input())
find = list(map(int,input().split()))

cnt = {}
for c in card:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1

for i in find:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')

