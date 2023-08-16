print("Ingrese una figura:\n"\
          "1.circulo\n 2.Triangulo\n 3. Rectangulo")
fig=input("Seleccione una figura: ")
A="INVALIDO"; figura=fig

if (fig.lower()=="circulo") or (fig=='1'):
    r=eval(input("Ingrese el valor del radio: "))
    A=3.1416*r**2
elif (fig.lower()=="Triangulo") or (fig=='2'):
    b=int(input("Ingrese la base: "))
    h=eval(input("Ingrese la altura: "))
    A=(b*h)/2
    figura="Triangulo"
elif  (fig.lower()=="Rectangulo") or (fig=='3'):
    b=int(input("Ingrese la base: "))
    h=eval(input("Ingrese la altura: "))
    A=b*h
    figura="Rectangulo"
else:
    print("Selecciones  una figura valida")
print(" Para un ", figura, "el valor del area es: ",A)
    