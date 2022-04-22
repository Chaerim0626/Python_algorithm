arr = []

for i in range(1,10001):
    a = i
    for j in str(i):
        a += int(j) #저장완료
    arr.append(a)
for i in range(1,10001):
    if i not in arr:
        print(i)