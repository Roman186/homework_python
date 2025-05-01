def is_year_leap(numb):
    if numb % 4 == 0:
        return True
    else:
        return False


numb = int(input("Введите год: "))
result = is_year_leap(numb)
print(f"год {numb}: {result}")
