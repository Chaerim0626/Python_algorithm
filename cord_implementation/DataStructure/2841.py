import sys
line = [[] for _ in range(7)]
n, p = map(int, sys.stdin.readline().split())
cnt = 0
for _ in range(n):
    string, pr = map(int, sys.stdin.readline().split())
    if len(line[string]) == 0:
        line[string].append(pr)
        cnt += 1
    else:
        if line[string][-1] < pr:
            line[string].append(pr)
            cnt += 1
        elif line[string][-1] > pr:
            while line[string]:
                if line[string][-1] < pr or line[string][-1] == pr:
                    break
                line[string].pop()
                cnt+=1
            if len(line[string]) and line[string][-1] == pr:
                #줄이 안비어있고 마지막이 누른 pr과 같으면
                pass
            else:
                line[string].append(pr)
                cnt +=1
        else:
            pass
print(cnt)