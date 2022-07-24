import sys
input = sys.stdin.readline
arr = []
n = int(input())

for _ in range(n):
    i = int(input())
    arr.append(i)
arr.sort()

for i in arr:
    print(i)