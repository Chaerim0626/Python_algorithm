n=int(input())
arr = list(map(int, input().split()))
average=0
for i in arr:
    i=i/max(arr)*100
    average += i

print(average/n)