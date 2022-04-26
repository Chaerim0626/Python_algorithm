k = int(input())
arr = []
sum = 0
for i in range(k):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)

for i in arr:
    sum += i
print(sum)