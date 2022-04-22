from itertools import permutations
arr = [1,2,3,4,5,6,7,8,9]
num = list(permutations(arr,3)) #모든 3자리 수를 다 뽑아놓자
n= int(input())
for i in range(n):
    q, s, b = map(int, input().split())
