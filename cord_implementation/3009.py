x,y = map(int, input().split())
a,b = map(int, input().split())
c,d = map(int, input().split())
arr1 = [x,a,c]
arr2 = [y,b,d]
for i in range(3):
    if arr1.count(arr1[i]) == 1:
        resX = arr1[i]
    if arr2.count(arr2[i]) == 1:
        resY = arr2[i]
print(resX, resY)