n = int(input())
arr = []
for i in range(n):
    s = arr.append(input())
arr = set(arr)
arr = list(arr)

arr.sort(key=lambda x: (len(x), x))
for i in arr:
    print(i)