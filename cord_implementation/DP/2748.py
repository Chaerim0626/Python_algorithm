n = int(input())
arr = []

for i in range(n+1):
    if i ==0:
        num = 0
    elif i <= 2:
        num = 1
    else:
        num = arr[-1] + arr[-2]
    arr.append(num)
print(arr[n])