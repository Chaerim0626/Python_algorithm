import sys
input = sys.stdin.readline

s = input().rstrip()
set1 = set()
for i in range(len(s)):
    for j in range(i,len(s)):
        temp = s[i:j+1]
        set1.add(temp)
print(len(set1))