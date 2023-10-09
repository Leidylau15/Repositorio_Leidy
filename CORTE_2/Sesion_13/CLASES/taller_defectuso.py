def lectura():
    f = open("wcm.csv", "r", encoding="utf8")
    lines = f.readlines()
    listado = []
    for line in lines:
        fila = line.rstrip('\n').split(',')
        listado.append(fila)
    f.close()
    return listado

def tabla_de_datos(listado):
    campeones = {}
    for pais in listado:
       
def main():
    print('Seleccione una de las siguientes opciones:\n' \
         '1. Ver la tabla completa de participacion a los mundiales\n' \
         '2. Realizar la  busqueda por pais')
    
    listado = lectura()

    menu = {'1': tabla_de_datos,'2': buscar_por_pais}
       
    opcion = input('Seleccione una opción: ')

    if opcion in menu:
        menu[opcion](listado)
    else:
        print('Opción inválida')

if __name__ == "__main__":
    main()
