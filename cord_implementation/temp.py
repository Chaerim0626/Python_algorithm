def calcTime(city):
    time = cityList[city] / speed
    time = round(time, 1)
    return time

speed = 60
cityList = {'대구': 295.5, '대전': 167.9, '여수': 348.9}

print("{}까지는 총 {}시간 걸립니다.".format("대구", calcTime("대구")))
print("{}까지는 총 {}시간 걸립니다.".format("대전", calcTime("대전")))
print("{}까지는 총 {}시간 걸립니다.".format("여수", calcTime("여수")))