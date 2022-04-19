x, y, w, h = map(int, input().split())
arr = [x, y, w-x, h-y]
arr.sort()
print(arr[0])