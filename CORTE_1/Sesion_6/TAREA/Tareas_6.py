print("Ingrese el programa deseado: \n"\
      " 1.Divisores\n 2.Producto\n 3.Fibbonacci. ")
p=input("Selececione el programa: ")
if (p.lower() =="Divisore") or (p=="1"):
   n= int(input("Ingrese un número: "))
   if n == 0:
    print("Ningún número es divisible entre cero")
   else:
    print("Los divisores positivos de", n, "son:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

elif (p.lower()=="Producto") or (p=="2"):
   a = int(input("Ingrese un numero: "))
   b = int(input("Ingrese otro numero: "))

   producto = 0
   for i in range(abs(b)):
    producto += abs(a)

   if a < 0 and b < 0:
    producto = abs(producto)
   elif a < 0 or b < 0:
    producto = -producto
   print("Producto:",producto)

elif (p.lower()=="Fibonacci") or (p=="3"):

    N = int(input("Ingrese un numero entero positivo "))
    num1= 0
    num2= 1
    if N <= 0:
     print("La serie de Fibonacci es vacía.")
    elif N == 1:
     print("La serie de Fibonacci es:", num2)
    else:
     print("La serie Fibonnci es:  ")
    for i in range(N):
     print(num1, end= " ")
     num3= num1 + num2
     num1=num2
     num2=num3
else:
  print("Programa seleccionado invalido")