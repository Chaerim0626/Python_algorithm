import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

maxPaper = 0

def is_valid_coord(x,y):
    return 0 <= x < n and 0 <= y < m
shape = [
    #1
    [[0,0],[0,1],[0,2],[0,3]],
    [[0,0], [1,0], [2,0], [3,0]],

    #2
    [[0,0], [0,1], [1,0], [1,1]],

    #3
    [[0,0], [1,0], [2,0], [2,1]],
    [[0,0], [0,1], [0,2], [1,0]],
    [[0,0], [0,1], [1,1], [2,1]],
    [[0,0], [0,1], [0,2], [-1,2]],
    [[0,0], [0,1], [-1,1], [-2,1]],
    [[0,0], [0,1], [0,2], [1,2]],
    [[0,0], [0,1], [1,0], [2,0]],
    [[0,0], [1,0], [1,1], [1,2]],

    #4
    [[0,0], [1,0], [1,1], [2,1]],
    [[0,0], [0,1], [-1,1], [1,0]],
    [[0,0], [0,1], [-1,1], [-1,2]],
    [[0,0], [0,1], [1,1], [1,2]],

    #5
    [[0,0], [0,1], [0,2], [1,1]],
    [[0,0], [0,1], [0,2], [-1,1]],
    [[0,0], [1,-1], [1,0], [2,0]],
    [[0,0], [1,0], [2,0], [1,1]],

]
def tet(a,b):
    global maxPaper
    for i in range(19):
        sumPaper = 0
        for j in range(4):
            if is_valid_coord(a+shape[i][j][0],b+shape[i][j][1]):
                sumPaper += arr[a + shape[i][j][0]][b + shape[i][j][1]]
            else:
                break
            maxPaper = max(sumPaper, maxPaper)

for i in range(n):
    for j in range(m):
        tet(i,j)
print(maxPaper)