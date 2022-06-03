import sys
input = sys.stdin.readline

n, l, m = map(int, input().split())
stack = []
for i in range(m):
    y, x = map(int, input().split())
    stack.append([y,x])
# (a+b)*2 = 100, a+b = 50 최악의 경우  1,49, 2,48 .. -> 50개

def is_valid_coord(y,x):
    return 0 < x <= n and 0 < y <= n

def cnt(sy,sx,ey,ex):
    cntFish = 0
    if not is_valid_coord(ey,ex):
        return 0
    for y,x in stack:
        if sy <= y <= ey and sx <= x <= ex:
            cntFish +=1
    return cntFish

def getNet(l):
    nets = []
    for i in range(1,l//2):
        nets.append((i, l//2 - i)) #그물조합 대로 저장
    return nets

def move(net):
    fish = 0
    for y, x in stack:
        for ny in range(y,y-net[0]-1,-1):
            fish = max(fish, cnt(ny,x,ny+net[0],x+net[1]))
        for nx in range(x,x-net[1]-1,-1):
            fish = max(fish,cnt(y,nx,y+net[0],nx+net[1]))
    return fish

res = 0
for net in getNet(l):
    res = max(res,move(net))

print(res)

