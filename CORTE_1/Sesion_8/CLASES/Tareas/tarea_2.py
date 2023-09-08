#Ejercicio 2 

meses = {
    "Enero": (31, "Año Nuevo"),
    "Febrero": (28, "Día de San Valentín"),
    "Marzo": (31, "Día de San José"),
    "Abril": (30, "Semana Santa"),
    "Mayo": (31, "Día del Trabajo"),
    "Junio": (30, "Día del Padre"),
    "Julio": (31, "Día de la Independencia"),
    "Agosto": (31, "Día de la Madre"),
    "Septiembre": (30, "Día de la Independencia"),
    "Octubre": (31, "Día de la Raza"),
    "Noviembre": (30, "Día de los Muertos"),
    "Diciembre": (31, "Navidad"),
}


nombre_mes = input("Ingresa el nombre de un mes del año: ")


nombre_mes = nombre_mes.capitalize()

#
if nombre_mes in meses:
  
    num_dias, festivo = meses[nombre_mes]
    print(f"{nombre_mes} tiene {num_dias} días, incluyendo el festivo de {festivo}.")
else:
    print("El mes ingresado no es válido o no está en la lista.")
