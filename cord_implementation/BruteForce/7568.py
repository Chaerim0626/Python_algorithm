import sys
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a,b))

for i in arr:
    rank=1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank+=1
    print(rank, end=" ")


