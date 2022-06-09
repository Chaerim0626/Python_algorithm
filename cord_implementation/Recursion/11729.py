import sys
input = sys.stdin.readline

k = int(input())

def hanoi(n, a, b):
    if n > 1:
        hanoi(n-1, a, 6-a-b)
    print(a,b)

    if n > 1:
        hanoi(n-1, 6-a-b, b)

print(2**k-1)
hanoi(k,1,3)