x, y, p1, p2 = map(int, input().split())
arr1 = [p1]
arr2 = [p2]
res = -1
cnt =1
while cnt < 10001:
    p1 += x
    p2 += y
    arr1.append(p1)
    arr2.append(p2)
    if p1 in arr2:
        res = p1
        break
    elif p2 in arr1:
        res = p2
        break
    cnt+=1
print(res)
