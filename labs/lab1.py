#Задание 1
import math as m
x = int(input())
y = int(input())
z = int(input())

a = m.log10(abs(x-1)) + ((abs(x))**(1/4))/ (x**(1/4) + (abs(x)**(1/4) * m.log10(y)))

b = (abs(x-1)**(1/3)) + (m.cos(z)/m.tan(x**2))

print(a,b)

#Задание 2
def task2(x):
    a = 1
    b = 2
    return (a * (x ** 3) + x) / (b * (x ** 2)) + ((x ** 2) ** (1 / 3))


x = float(input(1))
print(task2(x))
