#Задание 1

def is_square(number):
    sqrt = int(number ** 0.5)  # Вычисляем корень числа и приводим к целому числу
    return sqrt * sqrt == number  # Проверяем, является ли квадратом целого числа


def is_palindrome(number):
    str_number = str(number)  # Преобразуем число в строку
    return str_number == str_number[::-1]  # Сравниваем число с обратной ему строкой


while True:
    num = int(input("Введите число: "))

    if is_square(num):
        print("Число является квадратом целого числа")
    else:
        print("Число не является квадратом целого числа")

    if is_palindrome(num) and len(str(num)) == 5:
        print("Число является пятизначным палиндромом")
    else:
        print("Число не является пятизначным палиндромом")
#Задание 3
number = float(input("Введите десятичную дробь: "))
base = int(input("Введите основание новой системы счисления: "))
integer_part = int(number)
res: str = ""
decimal_part = number - integer_part

while integer_part > 0:
    remainder = integer_part % base
    res = str(remainder) + res
    integer_part = integer_part // base

if decimal_part > 0:
    res += "."

while decimal_part > 0:
    decimal_part *= base
    current_digit = int(decimal_part)
    res += str(current_digit)
    decimal_part -= current_digit

print("Результат:", res)


#Задание 6
def months_to_buy(cost, salary):
    down_payment = cost * 0.05  # Размер первоначального взноса (5% от стоимости)
    monthly_savings = salary * 0.03  # Ежемесячное накопление (3% от заработной платы)
    months = 0

    while down_payment < cost:
        cost -= monthly_savings
        down_payment += monthly_savings
        months += 1

    return months

cost = 1000000  # Стоимость покупки
salary = 5000  # Заработная плата

num_months = months_to_buy(cost, salary)
print("Необходимое количество месяцев для накопления:", num_months)


print(months_to_buy(10000, 20000))

#Задание 10
import math

def arctan(x, n):
    result = 0
    for i in range(n+1):
        coef = (-1)**i
        num = x**(2*i+1)
        denom = 2*i+1
        result += coef * (num / denom)
        return result

def residual_error(x, n):
    c = x / 2 # выбираем c между 0 и x
    next_term = (-1)**(n+1) * (x**(2*n+3)) / (2*n+3)
    residual = abs(next_term)
    return residual

x = 0.5
n = 5
approximation = arctan(x, n)
error = residual_error(x, n)
actual_value = math.atan(x)

print(f"Частичная сумма ряда: {approximation}")
print(f"Актуальное значение арктангенса: {actual_value}")
print(f"Оценка остаточной ошибки: {error}")


#Задание 8
def calculate_sum(x, epsilon):
    term = 1/2
    result = term
    n = 1

    while abs(term) > epsilon:
        n += 1
        term *= (-1) * (n - 1) * x / n
        result += term

    return result

x = 0.5  # Заданное значение x
epsilon = 0.0001  # Заданная точность epsilon

sum_value = calculate_sum(x, epsilon)
print("Сумма ряда S =", sum_value)




#Задание 2

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x >= 0:
        return abs(x - 2) - 1
    else:
        return np.exp(x)

a = -5 # Начальное значение интервала
b = 5 # Конечное значение интервала
num_points = 100  # Количество точек для построения графика

x_values = np.linspace(a, b, num_points)
y_values = np.array([f(x) for x in x_values])

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid(True)
plt.show()


#Задание 5
def find_intersection(rect1, rect2):
    # Извлекаем координаты верхнего левого и нижнего правого углов прямоугольников
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    # Проверяем, пересекаются ли прямоугольники
    if x1 > x4 or x2 < x3 or y1 > y4 or y2 < y3:
        # Прямоугольники не пересекаются
        # Вычисляем расстояние между ближайшими вершинами
        distance = min(
            ((x1 - x4) ** 2 + (y1 - y4) ** 2) ** 0.5,  # Расстояние между вершинами (x1, y1) и (x4, y4)
            ((x2 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5,  # Расстояние между вершинами (x2, y1) и (x3, y3)
            ((x1 - x4) ** 2 + (y2 - y3) ** 2) ** 0.5,  # Расстояние между вершинами (x1, y2) и (x4, y3)
            ((x2 - x3) ** 2 + (y2 - y4) ** 2) ** 0.5   # Расстояние между вершинами (x2, y2) и (x3, y4)
        )
        return distance
    else:
        # Прямоугольники пересекаются
        # Вычисляем площадь пересечения
        intersection_width = min(x2, x4) - max(x1, x3)
        intersection_height = min(y2, y4) - max(y1, y3)
        intersection_area = intersection_width * intersection_height
        return intersection_area

# Пример использования
rect1 = (0, 0, 5, 5)
rect2 = (3, 3, 8, 8)
intersection_area = find_intersection(rect1, rect2)
print("Площадь пересечения:", intersection_area)

rect3 = (0, 0, 2, 2)
rect4 = (3, 3, 5, 5)
distance = find_intersection(rect3, rect4)
print("Расстояние между ближайшими вершинами:", distance)
