from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, K = map(int, input().split())

maxNum = 100000
visited = [0] * (maxNum + 1)

def bfs():
       dq = deque()
       dq.append(N)
       while dq:
          x = dq.popleft()
          if x == K:
             print(visited[x])
             break
          for j in (x-1,x+1,x*2):
            if 0 <= j <= maxNum and not visited[j]:
              visited[j] = visited[x]+1
              dq.append(j)

bfs()