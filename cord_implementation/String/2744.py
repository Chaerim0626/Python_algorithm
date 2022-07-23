t=""
for i in input():
    if i.islower():
        t += i.upper()
    else:
        t += i.lower()
print(t)