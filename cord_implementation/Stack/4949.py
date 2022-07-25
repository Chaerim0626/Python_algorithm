import sys
input = sys.stdin.readline

while True:
    text = input().rstrip()
    stack = []
    value = "yes"
    if text == ".":
        break
    for i in text:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                value = "no"
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                value = "no"
    if stack:
        value="no"
        print(value)
    else:
        print(value)
