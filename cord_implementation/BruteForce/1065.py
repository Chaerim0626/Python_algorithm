n = int(input())
cnt=0
for i in range(1,n+1):
    if i <100: cnt+=1
    else:
        a = str(i)
        for j in range(len(a)-2):
            if int(a[j+1]) - int(a[j]) == int(a[j+2]) - int(a[j+1]):
                cnt+=1
            else:break
print(cnt)