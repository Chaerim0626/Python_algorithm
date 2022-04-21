#브루포스트 알고리즘, 정렬
arr = [int(input()) for _ in range(9)]
sum = 0
sumValue = False
for i in range(9):
    sum += arr[i]

for i in range(9):
    for j in range(i+1,9):
        if arr[i] + arr[j] == (sum - 100):
            arr.pop(i)
            arr.pop(j-1)
            sumValue = True
            break
    if sumValue == True:break
arr.sort()
for i in arr:
    print(i)
