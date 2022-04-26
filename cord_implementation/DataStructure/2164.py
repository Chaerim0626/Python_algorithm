from collections import deque
n = int(input())
deq = deque()
#시간복잡도는 O(N)
for i in range(n,0,-1):
    deq.appendleft(i)
while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq.pop())
