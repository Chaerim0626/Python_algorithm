import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
chicken = []
house = []
cities = []
for i in range(n):
    cities.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if cities[i][j] == 1:
            house.append([i,j])
        elif cities[i][j] == 2:
            chicken.append([i,j])
res = 5000

for i in combinations(chicken, m):
    distance = 0
    for j in house:
        chickenLength = 50
        for k in range(m):
            chickenLength = min(chickenLength, abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]))
        distance += chickenLength
    res = min(res,distance)
print(res)