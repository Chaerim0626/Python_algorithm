n, k = map(int, input().split())
arr = []
for i in range(1,k+1):
    arr.append(int(str(n*i)[::-1]))

print(max(arr))
