from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline
n= int(input())
card1 = list(map(int, input().split()))
m=int(input())
card2 = list(map(int,input().split()))

card1.sort()

for i in range(m):
    if bisect_right(card1,card2[i]) - bisect_left(card1,card2[i]):
        card2[i] = 1
    else:
        card2[i] = 0

print(*card2)
print(' '.join(map(str, card2)))