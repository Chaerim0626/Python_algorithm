n= int(input())
i=1
res = []
stack = []
flag=True
for _ in range(n):
    num = int(input())
    if not stack:
        stack.append(i)
        res.append('+')
        i +=1
    if stack[-1] < num:
        while stack[-1] < num:
            res.append('+')
            stack.append(i)
            i += 1
    if stack[-1] == num:
        res.append('-')
        stack.pop()
    else: #stack[-1] > num일때
        print("NO")
        flag=False
        break

if flag==True:
    for i in res:
        print(i)