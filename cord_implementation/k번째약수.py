import sys
#sys.stdin=open("input.txt", "rt")

a, b = map(int, input().split()) #입력받은 값을 공백으로 분리
c = list()
for x in range(1, a+1):
    if a % x == 0:
        c.append(x)
    else:
        continue
  
if b-1 < len(c):
    print(c[b-1])
else:
    print(-1)
