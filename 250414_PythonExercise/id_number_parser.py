

id = "901212-1234567"

def birthday_parse(id):
    year = "19" + id[0:2]
    month = id[2:4]
    day = id[4:6]
    return f"{year}년 {month}월 {day}일"


print(birthday_parse(id))

