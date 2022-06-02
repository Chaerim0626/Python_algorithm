import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
stack = []
res = 0

def backTracking():
    global res
    if len(stack) == n:
        total = 0
        for i in range(n-1):
            total += abs(arr[stack[i]] - arr[stack[i+1]])
        res = max(res,total)

    else:
        for idx in range(n):
            if idx not in stack:
                stack.append(idx)
                backTracking()
                stack.pop()
print(res)