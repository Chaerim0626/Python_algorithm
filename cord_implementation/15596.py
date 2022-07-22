
def solve(a):
    res = 0
    for i in a:
        res += i
    return res

arr = list(map(int, input().split()))
print(solve(arr))