import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[n-1]
second = arr[n-2]

res = 0

while True:
    for i in range(k):
        if m == 0:
            break
        res += first
        m -= 1
    if m ==0:
        break
    res += second
    m -= 1

print(res)