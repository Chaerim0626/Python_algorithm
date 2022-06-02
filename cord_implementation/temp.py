#5214
from collections import deque

N, K, M = map(int, input().split())

# 0 ~ N-1: 역, N ~ N+M-1: 하이퍼튜브
adj = [[] for _ in range(N + M)]
for i in range(N, N + M):  # i: 하이퍼튜브
    for j in map(lambda x: x - 1, map(int, input().split())):  # j: 역
        adj[i].append(j)
        adj[j].append(i)


def bfs():
    chk = [False] * (N + M)
    chk[0] = True
    q = deque()
    q.append((0, 1))
    while q:
        now, d = q.popleft()

        if now == N - 1:
            return (d + 1) // 2

        nd = d + 1
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True
                q.append((nxt, nd))

    return -1


print(bfs())

