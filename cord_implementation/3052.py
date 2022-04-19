arr = [int(input()) for _ in range(10)]
for i in range(10):
    arr[i] = arr[i] % 42
res = len(set(arr))
print(res)
