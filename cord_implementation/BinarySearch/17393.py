import sys
input = sys.stdin.readline
from bisect import bisect_right,bisect_left
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = []
for idx, a in enumerate(A):
    print(bisect_right(B,a), bisect_left(B,a))
