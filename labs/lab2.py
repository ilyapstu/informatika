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
