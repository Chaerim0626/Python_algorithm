import sys
sys.stdin=open("input.txt", "rt")

# 2개의 자료 입력
n, k = map(int, input().split())
for num in range(n):
    a = list(map(int, input().split()))
    res = set()
    for i in range(n):
        for j in range(i+1, n):
            for m in range(j+1, n):
                res.add(a[i]+a[j]+a[m])
                #set은 sort기능 X
    res=list(res)
    res.sort(reverse=True) #내림차순
    print(res[k-1])
