import sys
input = sys.stdin.readline
n,m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())
for i in range(k):
    sum1 = 0
    i,j,x,y = map(int, input().split())
    for l in range(i-1,x):
        for m in range(j-1,y):
           sum1 += arr[l][m]
    print(sum1)