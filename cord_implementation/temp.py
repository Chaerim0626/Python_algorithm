import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list((map(int, input().split())))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2
    cutTree = 0

    for tree in trees:
        if tree > mid:
            cutTree += tree - mid #자른 나무수 갱신
    if cutTree < m :
        end = mid -1
    else:
        start = mid + 1
print(end)