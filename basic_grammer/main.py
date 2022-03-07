#값 교환
a, b = 10, 20
a, b = b, a

#출력 방식
a, b, c = 1, 2, 3
print(a, b, c, sep = ",") #,로 분리
print(a, b, c, sep = "")
print(a, b, c, sep = "\n")

#변수 입력과 연산자
a, b = input("숫자 입력 : ").split()
print(a, b)
print(a+b) #숫자 연결

c, d = map(int, input("숫자 입력 : ").split())
print(c+d) #정수형

#조건문 if(분기, 중첩)
x = 7
if x ==7:
    print("Lucky")

x = 15 #중첩
if x >= 10:
    if x%2 == 1:
        print("10이상의 홀수")

x = 10 #분기
if x > 0:
    print("양수")
else:
    print("음수")