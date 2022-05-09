import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = [input().rstrip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dq = deque()


while dq:
    x, y = dq.popleft()

    if x == n-1 and y == m-1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and board[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] +1
                dq.append((nx,ny))
