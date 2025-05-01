from math import ceil


def square(a):
    area = a ** 2
    return ceil(area)


a = float(input("введите длину стороны квадрата: "))
result = square(a)
print(result)
