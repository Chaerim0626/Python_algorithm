t = int(input())
for i in range(t):
    arr = list(input())
    num = len(arr)
    n=1
    score=0
    for j in range(num):
        if j == 0 and arr[j] == 'O': #처음 경우
            score += 1

        elif arr[j-1] == 'X' and arr[j] == 'O':
            score += 1

        elif arr[j-1] == 'O' and arr[j] == 'O':
            n += 1
            score += n
        elif arr[j] == 'X':
            n = 1
    print(score)
