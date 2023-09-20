import math as m
x = int(input())
y = int(input())
z = int(input())

a = m.log10(abs(x-1)) + ((abs(x))**(1/4))/ (x**(1/4) + (abs(x)**(1/4) * m.log10(y)))

b = (abs(x-1)**(1/3)) + (m.cos(z)/m.tan(x**2))

print(a,b)
