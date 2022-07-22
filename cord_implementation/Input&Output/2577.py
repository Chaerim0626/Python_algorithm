a = int(input())
b = int(input())
c = int(input())
res = a*b*c
num = [0,1,2,3,4,5,6,7,8,9]
count = [0]*10
for i in str(res):
    for j in num:
        if int(i) ==j:
            count[j] += 1
for i in count:
    print(i)