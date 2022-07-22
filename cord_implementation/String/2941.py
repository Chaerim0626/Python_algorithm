s = input()
cnt = 0

for i in range(len(s)):
    i=0
    if 'c=' in s:
        s = s.replace('c=','0')
    elif 'c-' in s:
        s = s.replace('c-','0')
    elif 'dz=' in s:
        s = s.replace('dz=','0')
    elif 'd-' in s:
        s = s.replace('d-','0')
    elif 'lj' in s:
        s = s.replace('lj','0')
    elif 'nj' in s:
        s = s.replace('nj', '0')
    elif 's=' in s:
        s = s.replace('s=','0')
    elif 'z=' in s:
        s = s.replace('z=','0')

cnt += len(s)
print(cnt)
