import sys
input = sys.stdin.readline
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt=0
for i in range(1,n+1):
       arr2= combinations(arr,i)
       for x in arr2:
              if sum(x) == s:
                     cnt +=1
print(cnt)