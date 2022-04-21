while True:
    b,n= map(int, input().split())
    if b == 0 and n == 0:break
    a=0
    while pow(a+1,n) < b:
        a += 1
    if b - pow(a,n) < pow(a+1,n) - b:
        print(a)
    else:
        print(a+1)

