import sys
input = sys.stdin.readline

n= int(input())
arr = []
for i in range(n):
    age,name = map(str,input().split())
    arr.append([int(age), name,i])

arr.sort(key=lambda x: (x[0],x[2]))
for i in arr:
    print(i[0], i[1])
