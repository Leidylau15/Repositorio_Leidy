import math as math 

a=int(input('Ingrese el valor de a: '))
b=int(input('Ingrese el valor de b: '))
c=int(input('Ingrese el valor de c: '))
x1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
x2=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
print('La Solucion es' ,x1, 'y' ,x2)
