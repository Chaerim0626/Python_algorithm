import math
while True:
    b,n= map(int, input().split())
    if b == 0 and n == 0:
        break
    a=1
    while pow(a,n) < b:
        a += 1

    print( a-1 if b-pow(a-1,n) < pow(a,n) - b else a)


