t = int(input())

for i in range(t):
    r,s = input().split()
    r = int(r)
    res=""
    for j in s:
        res += r*j
    print(res)
