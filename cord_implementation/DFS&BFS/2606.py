import sys
input = sys.stdin.readline
n= int(input())
graph = [[]*(n+1) for _ in range(n+1)]

connect = int(input())
for i in range(connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

chk = [False]*(n+1)
def dfs(num):
    chk[num] = True
    for i in graph[num]:
        if chk[i] == False:
            dfs(i)

dfs(1)
print(chk.count(True)-1)