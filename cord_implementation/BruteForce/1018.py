n,m = map(int, input().split())
cnt = []
arr = []
for i in range(n):
    arr.append(input())

for i in range(n-7):
    for j in range(m-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0: #짝수지점
                    if arr[k][l] != 'W':
                        first_W = first_W + 1
                    else:
                        first_B = first_B + 1
                else:
                        if arr[k][l] != 'B':
                            first_W = first_W + 1
                        else:
                            first_B = first_B + 1
        cnt.append(min(first_W,first_B))
print(min(cnt))



