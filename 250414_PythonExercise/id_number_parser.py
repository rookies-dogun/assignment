def birthday_parse(id):
    return f"{"19" + id[0:2]}년 {id[2:4]}월 {id[4:6]}일"

id = "901212-1234567"
print(birthday_parse(id))

