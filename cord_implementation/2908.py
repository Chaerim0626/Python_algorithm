a, b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
a = ''.join(a)
b = ''.join(b)

a = int(a)
b = int(b)

print(a) if a > b else print(b)