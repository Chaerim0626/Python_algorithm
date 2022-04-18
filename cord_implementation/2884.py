h, m = map(int, input().split())
if m >= 45:
    print(h, m-45)
elif h == 0: #0시고 분이 45분 보다 작은 경우
    h = 23
    print(h,60-(45-m))
else: # 0시도 아니고 45분보다 작은경우
    print(h-1, 60-(45-m))
