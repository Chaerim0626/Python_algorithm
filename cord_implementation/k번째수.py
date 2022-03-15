import sys
sys.stdin=open("input.txt", "rt")

T=int(input()) #case개수
for t in range(T):
    n, s, e, k = map(int, input().split()) #띄어서 맵핑
    a = list(map(int, input().split())) #한 줄 읽어서 list화
    a = a[s-1:e] #s번째부터 e번째까지 추출
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))