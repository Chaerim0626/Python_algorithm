arr = []
n=1

while n < 1001:
    arr.append(int(n*(n+1)/2))
    n+=1

num = int(input())
for i in range(num):
    flag=False
    t = int(input())
    for j in range(t):
        for k in range(t):
            for l in range(t):
                if arr[j] + arr[k] + arr[l] == t:
                    flag=True
                    break
            if flag==True:break
        if flag==True:break
    print(1) if flag==True else print(0)




