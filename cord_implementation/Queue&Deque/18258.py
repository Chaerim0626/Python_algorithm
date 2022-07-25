import sys
input = sys.stdin.readline
from collections import deque

q = deque()
n = int(input())

for i in range(n):
    text = input().rstrip()
    if text == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif text == "size":
        print(len(q))
    elif text == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif text == "front":
        if q:
            num = q.popleft()
            print(num)
            q.appendleft(num)
        else:
            print(-1)
    elif text == "back":
        if q:
            num = q.pop()
            print(num)
            q.append(num)
        else:
            print(-1)
    else:
        q.append(text[5:])