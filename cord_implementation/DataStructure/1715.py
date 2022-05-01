import sys
import heapq
input = sys.stdin.readline

hq = []
sum = 0
n= int(input())
for _ in range(n):
    num = int(input())
    heapq.heappush(hq,num)
while len(hq) > 1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    c = a+b
    sum += c
    heapq.heappush(hq,c)

print(sum)
