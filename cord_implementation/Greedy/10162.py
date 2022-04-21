t = int(input())
a = 300
b = 60
c = 10

x= 0
y = 0
z = 0

if t // a == 0:
    if t // b == 0:
        if t % c != 0:
            print(-1)
        else:#나머지 0일경우
            z += t //c
            print(x, y, z)

    else:
        y = t // b
        t -= y*60
        if t % c == 0: #나머지 0 일 경우
            z = t //c
            print(x, y, z)

        else: #나머지 0 아닐 경우
            print(-1)


else:
    x = t// a
    t -= x*300
    if t // b == 0:
        if t % c ==0:
            z += t//c
            print(x, y, z)

        else:
            print(-1)
    else:
        y = t // b
        t -= y*60
        if t % c == 0:
            z += t //c
            print(x, y, z)

        else:
            print(-1)

