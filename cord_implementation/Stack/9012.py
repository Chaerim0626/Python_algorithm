n = int(input())

for i in range(n):
    s = list(input())
    isVPS = True
    stack = []
    for j in range(len(s)):
        if s[j] == '(':
            stack.append(s[j])
        else: #j번째 원소가 ')'인데
            if stack: # 안비어있다
                stack.pop()
            else: #)가 나왔는데 비어있다? )개수가 더 많겠죠
                print("NO")
                isVPS = False
                break

    if stack and isVPS == True: #안비어있으면 (개수가 더 많겠죠
        print("NO")
    elif not stack and isVPS == True:
        print("YES")


