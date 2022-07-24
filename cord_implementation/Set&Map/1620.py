import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = {}
for i in range(1,n+1):
    po = input().rstrip()
    dic[i] = po
    dic[po] = i

for i in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(dic[int(q)])
    else:
        print(dic[q])