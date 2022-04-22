n = int(input())
num = []
i=666
while True:
    a = str(i)
    cnt6=0
    for j in range(len(a)-2):
        if a[j] == '6' and a[j+1] == '6' and a[j+2] == '6':
            num.append(i)
            break
    i+=1
    if len(num) > 10000:
        break

print(num[n-1])


