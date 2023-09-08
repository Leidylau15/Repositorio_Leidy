# Ejercicio 1 
import random as rd
rd_numero= [rd.randint(1, 100) for _ in range(15)]
print("los numeros aleatorios son: ", rd_numero)
rd_numero.sort()
print('los numero ordenados de menor a mayor son:')
print(rd_numero)
 
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

nombre_mes =input("Ingresa el nombre de un mes del año: ").lower()
nombre_mes = nombre_mes.lower()
if nombre_mes in meses:
    info_mes = meses[nombre_mes]
    dias = info_mes["dias"]
    festivos = info_mes["festivos"]
    print(f"{nombre_mes.lower()} tiene {dias} días.")
    if festivos:
        print("Festivos:")
        for festivo in festivos:
            print(f"- {festivo}")
    else:
        print("No hay festivos en este mes.")
else:
    print("El mes ingresado no es válido.")
