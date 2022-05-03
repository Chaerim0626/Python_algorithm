import sys
import heapq
hq = []
n,m = map(int, sys.stdin.readline().split())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))
present = True
for i in arr1:
    heapq.heappush(hq,-i)

for j in range(m):
    num = -(heapq.heappop(hq))
    if num >= arr2[j]:
        heapq.heappush(hq,arr2[j]-num)
    else:
        present=False
        break
print(1 if present==True else 0)


