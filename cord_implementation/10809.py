s = list(input())
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alpha)):
    if alpha[i] in s:
        alpha[i] = s.index(alpha[i])
    else:
        alpha[i] = -1
for i in alpha:
    print(i, end=" ")
