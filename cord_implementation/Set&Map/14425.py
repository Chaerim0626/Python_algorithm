import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr1 = []
arr2 = []
cnt = 0
for i in range(n):
    s1 = input()
    arr1.append(s1)

for i in range(m):
    s2 = input()
    if s2 in arr1:
        cnt += 1
print(cnt)