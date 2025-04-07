import re

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
user_email = input("이메일 주소 :")

if re.match(pattern, user_email):
    print("유효함")
else:
    print("유효하지 않음")