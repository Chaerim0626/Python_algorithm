import sys
input = sys.stdin.readline
h, w = map(int, input().split())
arr = list(map(int, input().split()))

water = 0

for i in range(1,w-1):
    left = max(arr[:i])
    right = max(arr[i+1:])

    tmp = min(left, right)

    if arr[i] < tmp:
        water += tmp - arr[i]

print(water)