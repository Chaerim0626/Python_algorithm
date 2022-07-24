import sys
input = sys.stdin.readline
a,b = map(int,input().split())

set1 = set(map(int,input().split()))
set2 = set(map(int,input().split()))

s1 = len(set1-set2)
s2 = len(set2-set1)
print(s1+s2)