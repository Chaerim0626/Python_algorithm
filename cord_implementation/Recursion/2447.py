import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
stars = ["***", "* *", "***"]
def makeStar():
    L = len(stars)
    board = []
    for i in range(3*L):
        if i // L == 1:
            board.append(stars[i%L] + " "*L + stars[i%L])
        else:
            board.append(stars[i%L]*3)
    return board

while n > 3:
    n /= 3
    cnt += 1

for i in range(cnt):
    stars = makeStar()

for i in stars:
    print(i)