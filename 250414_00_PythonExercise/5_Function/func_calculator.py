

def calculator(a, b, op):
    if(op == "+"):
        return a + b
    elif(op == "-"):
        return a - b
    elif(op == "*"):
        return a * b
    elif(op == "/"):
        return a / b
    else:
        return "오류 입력입니다."


print(calculator(1, 2, "*"))


