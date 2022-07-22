s = input()
arr = list(s.split(" "))
n = len(arr)
if arr[0] == "" and arr[-1] == "":
    n-=2
elif arr[-1] == "":
    n -= 1
elif arr[0] == "":
    n -=1
print(n)