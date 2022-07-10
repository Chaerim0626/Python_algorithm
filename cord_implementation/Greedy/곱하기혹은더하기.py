import sys
input = sys.stdin.readline

s = input().strip()
stack = []

for i in range(len(s)):
    stack.append(int(s[i]))

res = stack[0]

for i in range(1,len(stack)):
    if res == 0 or res == 1:
        res += stack[i]
    else:
        if stack[i] == 0 or stack[i] == 1:
            res += stack[i]
        else:
            res *= stack[i]

print(res)