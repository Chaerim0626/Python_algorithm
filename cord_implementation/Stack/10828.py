import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    text = input().rstrip()
    if text == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif text == "size":
        print(len(stack))
    elif text == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif text == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(text[5:])


