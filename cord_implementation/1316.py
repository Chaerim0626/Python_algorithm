import sys
n = int(input())
for i in range(n):
    word = sys.stdin.readline()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+2:]:
            n -= 1
            break

print(n)

