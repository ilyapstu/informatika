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
    months = 0
    quarterly_salary = salary
    while cost > 0:
        cost *= 1.0315  # Увеличиваем цену компьютера на 3.15%
        if months % 3 == 0 and months > 0:
            quarterly_salary *= 1.05  # Увеличиваем зарплату каждый квартал на 5%
            cost -= quarterly_salary
            months += 1
        return months


print(months_to_buy(10000, 20000))
