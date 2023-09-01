def main(fila,columna):
    matriz=[]
    for i in range(fila):
        matriz.append([])
        for j in range(columnas):
            num=int(input(f"Ingrese el numero de la poscicion [{i}],[{j}]:"))
            matriz[i].append(num)
    for i  in matriz:
        print(i)
    #return matriz

if __name__=="__main__":
    filas=int(input("Ingrese el numero de filas:"))
    columnas=int(input("Ingrese en numero de columnas:"))
    print(main(filas,columnas))
    