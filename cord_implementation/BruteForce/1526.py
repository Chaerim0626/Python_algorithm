n = int(input())
arr = []
flag = False
for j in range(1,n+1):
    for i in str(j):
        if i == '4' or i == '7':
            flag = True
        else:
            flag=False
            break

    if flag==True:
        arr.append(j)

print(max(arr))