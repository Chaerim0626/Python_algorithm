import sys
input = sys.stdin.readline
n = int(input())
arr = []
result = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    score = 0
    for j in range(1, len(arr[i])):
        score += arr[i][j]
    score /= arr[i][0]
    result.append(score)

for i in range(n):
    stu = 0
    for j in range(1,len(arr[i])):
        if arr[i][j] > result[i]:
            stu += 1
    per = stu/arr[i][0]*100
    print(f'{per:.3f}%')
