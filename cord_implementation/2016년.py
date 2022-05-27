def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    days = b
    if a == 1:
        answer = day[days%7]
    elif a == 2:
        days += 31
        answer = day[days%7]
    elif a == 3:
        days += 31 + 29
        answer = day[days%7]
    elif a == 4:
        days += 31 + 29 + 31
        answer = day[days%7]
    elif a == 5:
        days += 31 + 29 + 31 + 30
        answer = day[days%7]
    elif a == 6:
        days += 31 + 29 + 31 + 30 + 31
        answer = day[days%7]
    elif a == 7:
        days += 31 + 29 + 31 + 30 + 31 + 30
        answer = day[days%7]
    elif a == 8:
        days += 31 + 29 + 31 + 30 + 31 + 30 + 31
        answer = day[days%7]
    elif a == 9:
        days += 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
        answer = day[days%7]
    elif a == 10:
        days += 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30
        answer = day[days%7]
    elif a == 11:
        days += 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        answer = day[days%7]
    elif a == 12:
        days += 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        answer = day[days%7]
    return answer