def money_divide():


    share = int(10000 / 3)
    reminder = 10000 % 3
    return f"share = {share}, reminder = {reminder}"

print(money_divide())