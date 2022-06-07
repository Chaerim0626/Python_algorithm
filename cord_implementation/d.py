import re

def sendEmail(addr):
    # 소문자 a-z 대문자 A-Z : 2~3, 유효성 검사
    reg = '^[a-zA-Z0-9.+_-]+@[a-zA-z0-9]+\.[a-zA-Z]{2,3}$'
    if bool(re.match(reg, "codelion.example@gmail.com")):
        smtp.send_message(message)
    else:
        print("유효한 이메일 주소가 아닙니다.")