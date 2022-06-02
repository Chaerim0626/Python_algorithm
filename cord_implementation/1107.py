import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

if m:
    buttons = list(map(int,input().split()))
else:
    buttons = []

res = abs(100-n)
#최악의 경우 100번에서 500000까지 가야함 -> 499900 번 눌러야함
for i in range(1000001):
    k = str(i)
    for j in range(len(k)):
        if int(k[j]) in buttons:
            break
        elif j == len(k)-1:
            res = min(res, abs(i-n) + len(k))
print(res)
