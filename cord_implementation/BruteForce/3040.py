arr = ([int(input()) for _ in range(9)])

for i in range(8):
    for j in range(i+1,9):
        if sum(arr) - arr[i] - arr[j] == 100:
            a, b = i, j
            break
del arr[a]
del arr[b-1] #리스트의 길이가 하나 줄어드므로
for k in arr:
    print(k)





