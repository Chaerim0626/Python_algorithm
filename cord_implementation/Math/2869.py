import sys
input = sys.stdin.readline

a,b,v = map(int,input().split())
high = v- a #마지막엔 결국 a만큼 올라감
if high %(a-b) == 0: #V-A의 높이만큼 A-B의 속도를 구함
    day = high//(a-b)
else:
    day = high//(a-b) + 1
    #소수점으로 나오는 경우도 하루를 더올라가야함

print(day+1)