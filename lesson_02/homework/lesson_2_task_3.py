import math

num = math.ceil(float(input('Введите сторону квадрата: ')))


def square(num):
    return num * num


result = square(num)
print(result)
