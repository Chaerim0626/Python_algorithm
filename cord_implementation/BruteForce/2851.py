arr = [int(input()) for _ in range(10)]
res = 0
score = 0

for i in range(10):
    score += arr[i]
    if 100 - res >= abs(100-score):
        res = score
print(res)

