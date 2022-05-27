def solution(price, money, count):
    price2 = 0
    for i in range(1, count + 1):
        price2 += i * price

    answer = money - price2
    if answer >= 0:
        answer = 0
    else:
        answer = abs(answer)

    return answer