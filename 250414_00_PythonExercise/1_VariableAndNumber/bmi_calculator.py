weight = int(input("체중(kg):"))
height = int(input("키(cm):"))

bmi = round(weight / ((height / 100 ) ** 2), 1)
print(bmi)