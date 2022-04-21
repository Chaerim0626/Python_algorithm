n = int(input())
total = 0
for i in range(1,n+1):
    total += str(i).count("3")+str(i).count("6")+str(i).count("9")
print(total)