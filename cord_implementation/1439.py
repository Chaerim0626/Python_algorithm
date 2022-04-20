s = input()
cnt1 = 0
cnt2 = 0
if s[0] == '1':
    cnt1+=1
else:
    cnt2 +=1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            cnt1 +=1
        else:
            cnt2 +=1
print(cnt1) if cnt1 < cnt2 else print(cnt2)