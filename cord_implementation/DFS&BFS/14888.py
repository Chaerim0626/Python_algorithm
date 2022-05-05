import sys
input = sys.stdin.readline
N = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxRes = -1000000000
minRes = 1000000000

def sol(res, i, add, sub, mul, div):
    global maxRes
    global minRes
    if i == N:
       maxRes = max(maxRes, res)
       minRes = min(minRes, res)
       return
    if add >0:
       sol(res+number[i],i+1,add-1,sub,mul,div)
    if sub >0:
       sol(res-number[i],i+1,add,sub-1,mul,div)
    if mul>0:
       sol(res*number[i],i+1,add,sub,mul-1,div)
    if div>0:
        if res < 0:
            sol(-(-res//number[i]), i + 1, add, sub, mul, div-1)
        else:
            sol(res//number[i], i + 1, add, sub, mul, div-1)

sol(number[0],1,add,sub,mul,div)
print(maxRes)
print(minRes)