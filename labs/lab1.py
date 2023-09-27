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
S_shar = s/6 * m.pi
print(S_shar)


#Задание 5
m1 = float(input())
m2 = float(input())
F = float(input())
g = 6.67 * 10**-11 #постоянная 
r = (g * m1 * m2 / F)**(1/2)
print(r)
