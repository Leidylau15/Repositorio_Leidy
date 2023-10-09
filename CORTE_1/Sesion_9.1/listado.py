from pprint import pprint

def lectura():
    with open("wcm.csv", "r", encoding="utf8") as f:
        lines = f.readlines()
    listado = []
    for line in lines:
        fila = line.rstrip('\n').split(',')
        listado.append(fila)
    return listado

def main():
    listado = lectura()
    
    # Verificar si la matriz tiene suficientes filas y columnas
    if len(listado) >= 3 and len(listado[0]) >= 6:
        valor_posicion_3 = listado[2][2]  # Obtiene el valor en la posición 3 (fila 2, columna 2)
        valor_posicion_5 = listado[2][4]  # Obtiene el valor en la posición 5 (fila 2, columna 4)

        print(f"Valor en la posición 3: {valor_posicion_3}")
        print(f"Valor en la posición 5: {valor_posicion_5}")
    else:
        print("La matriz no tiene suficientes filas y/o columnas para obtener las posiciones 3 y 5.")

if __name__ == "__main__":
    main()


