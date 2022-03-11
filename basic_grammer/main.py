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

#반복문 (for, while)
a = range(10) #0~9
a = range(1, 10) #1~9
print(list(a))

for i in range(10):
    print(i)

for i in range(10, 0, -1): #10~1
    print(i)

i=1
while i<10:
    print(i)
    i = i+1

i=1
while True:
    print(i)
    if i==10:
        break
    i+=1

for i in range(1, 11):
    if i%2==0:
        continue
    print(i)

for i in range(1, 11):
    print(i)
    if i>15:
        break
    else: #11까지 출력
        print(11)

#반복문을 이용한 문제풀이
#1. 1~N 홀수 출력하기
n = int(input())
for i in range(1, n+1):
    if i % 2 == 1:
        print(i)

#2. 1~N까지의 합 구하기
n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum+i
print(sum)

#3. N의 약수
n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')

#중첩 반복문(2중 for문)
for i in range(5):
    print('i :', i, sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()

for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()

#문자열과 내장함수
msg = "It is time"
print(msg.upper())
print(msg.lower())
tmp = msg.upper()
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[:2]) #0, 1 출력
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end='')

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end='')

for x in msg:
    if x.islower():
        print(x, end='')

for x in msg: #알파벳만 출력
    if x.isalpha():
        print(x, end='')

tmp = 'AZ'
for x in tmp:
    print(ord(x)) #아스키 코드 출력

tmp = 65
print(chr(tmp))


#리스트와 내장함수(1)
import random as r
a=[]
b=list()
a=[1, 2, 3, 4, 5]
b=list(range(1,11)) #1~10까지 초기화
c = a+b
a.append(6)

a.insert(3, 7) #3번 인덱스에 7넣기

a.pop() #맨 뒷자리 빼기
a.pop(3) #3번인덱스 빼기

a.remove(4) #4라는 값 지우기
a.index(5) #5의 인덱스 출력

a=list(range(1, 11))
sum(a) #55
max(a) #10

r.shuffle(a) #섞기
a.sort() #오름차순
a.sort(reverse=True) #내림차순
a.clear() #빈리스트

#리스트와 내장함수(2)
a = [23, 12, 36, 53, 19]
print(a[:3])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in enumerate(a): # (0, 23)의 형태로 자료를 넘겨줌
    print(x)

b=(1, 2, 3, 4, 5) #튜플 값은 수정 불가
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])

for index, value in enumerate(a): #인덱스와 원소값 동시 접근
    print(index, value)

if all(60>x for x in a): #all은 모두가 참이어야 참
    print("Yes")
else:
    print("NO")

if any(15>x for x in a): #any는 한번이라도 참이면 참
    print("YES")
else:
    print("NO")


#2차원 리스트의 생성과 접근
a = [[0]*3 for _ in range(3)] #1차원 리스트 3번 반복
#표로 해석하기

for x in a:
    for y in x:
        print(y, end=' ') #리스트 출력

#함수 만들기




