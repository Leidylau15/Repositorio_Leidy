def lectura():
    with open("wcm.csv", "r", encoding="utf8") as f:
        lines = f.readlines()
    listado = []
    for line in lines:
        fila = line.rstrip('\n').split(',')
        listado.append(fila)
    return listado

def tabla_de_datos(listado):
    participacion = {}
    for fila in listado[1:]:  # Excluir la primera fila que contiene los encabezados
        home_team, away_team, year = fila[0], fila[1], fila[-1]
        if home_team in participacion:
            participacion[home_team].append(year)
        else:
            participacion[home_team] = [year]
        # Contar las participaciones del equipo visitante
        if away_team in participacion:
            participacion[away_team].append(year)
        else:
            participacion[away_team] = [year]
    # Calcular el número total de participaciones por país
    total_participaciones_por_pais = {}
    for pais, participaciones in participacion.items():
        total_participaciones = len(set(participaciones)) # Utiliza un conjunto para eliminar duplicados
        total_participaciones_por_pais[pais] = total_participaciones

    # Imprimir los resultados dentro de la función
    print("\n--------------------------Listado de participaciones --------------------\n")
    for pais, participaciones in total_participaciones_por_pais.items():
        print(f"{pais}: {participaciones} participaciones ")

def buqueda_de_pais(listado):
    pais_a_buscar = input("¿Qué país desea consultar? ").lower()  # Convertir la entrada a minúsculas
    participacion = {}
    
    for fila in listado[1:]:
        home_team, away_team, year = fila[0], fila[1], fila[-1]
        
        # Verifica si el país buscado está en el partido como equipo local o visitante
        if home_team.lower() == pais_a_buscar or away_team.lower() == pais_a_buscar:
            if pais_a_buscar in participacion:
                participacion[pais_a_buscar].append(year)
            else:
                participacion[pais_a_buscar] = [year]
    
    if pais_a_buscar in participacion:
        años = list(set(participacion[pais_a_buscar])) 
        orden_años= sorted(años, reverse=True) # Convierte a conjunto y luego a lista
        años_str = ', '.join(orden_años)  # Unir los años sin duplicados con comas
        total_participaciones = len(orden_años)
        
        print(f"{pais_a_buscar} ha participado {total_participaciones}\n veces en los años: {años_str}")
    else:
        print(f"{pais_a_buscar} no ha participado en la Copa del Mundo.")


def main():
    print('Seleccione una de las siguientes opciones:\n' \
         '1. Ver la tabla completa de participación en los mundiales\n' \
         '2. Realizar la búsqueda por país')
    
    listado = lectura()

    menu = {'1': tabla_de_datos, '2': buqueda_de_pais}
    opcion = input('Seleccione una opción: ')

    if opcion in menu:
        menu[opcion](listado)
    else:
        print('Opción inválida')

if __name__ == "__main__":
    main()
