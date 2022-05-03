import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = [input().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dq = deque()
dq.append((0,0))
visited[0][0] = 1

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
