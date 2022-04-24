n,K = map(int, input().split())
cnt = 0
x = str(K)
for i in range(n+1):
    if i < 10: i = '0'+str(i)
    for j in range(60):
        if j < 10: j = '0' + str(j)
        for k in range(60):
            if k < 10: k = '0' + str(k)
            if x in str(i) or x in str(j) or x in str(k):
                cnt+=1

print(cnt)
