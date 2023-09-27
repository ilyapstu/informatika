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


#Задание 3
import math as m
x = float(input())


def f(x):
    return (m.log10(m.cos(x ** (1 / 3)))) ** (1 / 3)


print(f(x))



#Задание 4
import math as m
s = float(input())
d =1
S_shar = s/6 * m.pi #формула поверхности шара, преобразована из S пов.куба
print(S_shar)


#Задание 5
m1 = float(input())
m2 = float(input())
F = float(input())
g = 6.67 * 10**-11 #постоянная 
r = (g * m1 * m2 / F)**(1/2)
print(r)


#Задание 6

h = int(input())
r = int(input())
S_osn = 2 * h * 4 * r   #формула площади боковой поверхности


print(S_osn)



#Задание 7
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
c1 = int(input())
c2 = int(input())
d = a1 * b2 - a2 * b1
x = ((c1 * b2) - (c2 * b1)) / d
y = ((a1 * c2) - (a2 * c1)) / d
c1 = (a1 * x) + (b1 * y) #Исправить c1 и c2
c2 = (a2 * x) + (b2 * y)

print((c1, c2))
print(round(y, 4))
