#Condicionales
print("Ingrese el programa deseado:\n"\
      "1. Abecedario\n2. Estacionamiento\n3. Triangulos")
p = input("Seleccione el programa: ")

if (p.lower() == "abecedario") or (p == "1"):
    l = input("Ingrese una letra del abecedario: ")
    if l.lower() in 'aeiou':
        print("La letra ingresada es una vocal")
    else:
        print("La letra ingresada es una consonante")

elif (p.lower() == "estacionamiento") or (p == "2"):
    e = float(input("Ingrese el tiempo de parqueo en minutos: "))
    v = e * 139
    p = (v * 19) / 100
    i = v + p
    t = round(i, 5)
    print("Tiempo de parqueo:", e, "minutos")
    print("Su base es:", v, "pesos\n"
          "El valor del iva es:", p,
          "\nEl total a pagar es:",round(i,2), "\n")

elif (p.lower() == "triangulos") or (p == "3"):
    lado_a = int(input("Ingrese la longitud de lado_a: "))
    lado_b = int(input("Ingrese la longitud de lado_b: "))
    lado_c = int(input("Ingrese la longitud de lado_c: "))
    if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
        print("Segun los valores para la longitud\nde lado a:", lado_a,
              "\nde lado b:", lado_b, "\ny para el lado c:", lado_c,
              "\nSe puede formar un triangulo")
        if (lado_a == lado_b) and (lado_b == lado_c):
            print("Y es un triangulo Equilatero")
        elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
            print("Y es un triangulo Isósceles")
        else:
            print("Y es un triangulo Escaleno")
    else:
        print("Las longitudes dadas no forman un triangulo, segun el teorema de desigualdad.")
else:
    print("Programa seleccionado invalido")