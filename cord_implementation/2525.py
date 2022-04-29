import sys
a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
h= a
m =b+c
if b + c >= 60:
    h += (b+c) //60
    while m >= 60:
        m -= 60

if h >= 24:
    print(h-24,m)
else:
    print(h,m)


