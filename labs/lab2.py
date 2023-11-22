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
