def f(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return f(20,20,20)
    if dp[a][b][c]: #값이 존재하면 리턴
        return dp[a][b][c]
    if a <b and b < c:
        dp[a][b][c] = f(a,b,c-1) + f(a,b-1,c-1) - f(a,b-1,c)
        return dp[a][b][c]
    dp[a][b][c] = f(a-1,b,c) + f(a-1,b-1,c) + f(a-1,b,c-1) - f(a-1,b-1,c-1)
    return dp[a][b][c]
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

while True:
    a,b,c, = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {f(a,b,c)}')


