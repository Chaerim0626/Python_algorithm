t = int(input())

for i in range(t):
    cnt = 0
    n, m = map(int,input().split())
    for j in range(n,m+1):
        for k in str(j):
            if k == '0': cnt+=1
    print(cnt)