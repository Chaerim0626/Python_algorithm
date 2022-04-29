import sys
n, m= map(int, sys.stdin.readline().split())
cnt=0
arr = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    arr.append(s)

for _ in range(m):
    text = sys.stdin.readline().rstrip()
    for i in arr:
        if text == i[:len(text)]:
            cnt += 1
            break

print(cnt)