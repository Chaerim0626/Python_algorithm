import sys
input = sys.stdin.readline
n=int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum=0
a.sort()
c = sorted(b, reverse=True)
for i in range(n):
    sum += a[i]*c[i]
print(sum)