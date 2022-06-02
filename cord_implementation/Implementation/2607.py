import sys
input = sys.stdin.readline

n = int(input())
words = []
firstAlpha = [0]*26
cnt = 0
for i in range(n):
    word = input().strip()
    words.append(word)

for i in words[0]:
    firstAlpha[ord(i)-65] +=1


for i in range(1,len(words)):
    alpha = firstAlpha[:]
    for j in words[i]:
        alpha[ord(j) - 65] -= 1 #뺀 값 저장

    if alpha.count(0) == 26:
        cnt+=1
    elif alpha.count(0) == 25 and alpha.count(-1) == 1:
        cnt+=1
    elif alpha.count(0) == 25 and alpha.count(1) == 1:
        cnt+=1
    elif alpha.count(0) == 24 and alpha.count(1) == 1 and alpha.count(-1) == 1:
        cnt+=1

print(cnt)