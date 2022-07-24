import sys
from collections import Counter as c
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    i = int(input())
    arr.append(i)

res1 = sum(arr) / n
res1 = int(round(res1,0))
arr.sort()
res2 = arr[len(arr)//2]
res4 = max(arr) - min(arr)

arr2 = c(arr)
mostCnt = arr2.most_common()
mostCnt_s = len(arr2.most_common())

if abs(res1) == 0:
    print(0)
else:
    print(res1)
print(res2)

if mostCnt_s > 1:
    if mostCnt[0][1] == mostCnt[1][1]:
        print(mostCnt[1][0])
    else:
        print(mostCnt[0][0])
else:
    print(mostCnt[0][0])

print(res4)