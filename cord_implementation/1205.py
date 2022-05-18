import sys
input = sys.stdin.readline

n, score, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)

    if score > scores[-1] or n+1 <= p:
        scores.append(score)
        scores.sort(reverse=True)
        print(scores.index(score)+1)
    else:
        print(-1)
else:
    print(1)