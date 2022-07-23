import sys
input = sys.stdin.readline
n,m = map(int,input().split())

pfs = list(map(int,input().split()))
for i in range(n-1):
    pfs[i+1] += pfs[i]

pfs = [0] + pfs #맨 앞에 0붙이기

for _ in range(m):
    i, j = map(int,input().split())
    print(pfs[j]-pfs[i-1])

df