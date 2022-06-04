import sys
input = sys.stdin.readline
from collections import deque
q = deque()
n = int(input())

def minAlpha(name):
    res = 0
    for i in name:
        res += min(ord(i) - 65, abs(ord(i) - 91))
    return res

def solve(name):
    minMove = len(name) -1 #한쪽으로만 이동

    for i in range(len(name)):
        idx = i + 1
        while idx < len(name) and name[idx] == 'A':
            idx += 1
        minMove = min(minMove, 2*i + len(name) - idx, 2*(len(name) - idx) + i)
    return minMove

for _ in range(n):
    name = input().strip()
    res = minAlpha(name) + solve(name)
    print(res)




