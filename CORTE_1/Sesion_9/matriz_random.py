from random import randint as r
def crear_matriz(fila,columna):
    matriz=[]
    for i in range(fila):
        matriz.append([])
        for j in range(columnas):   
           #num=int(input(f"Ingrese el numero de la poscicion [{i}],[{j}]:"))
           num=r(1,10)
           matriz[i].append(num)
    return matriz
    
def imprimir(matriz):
    for i  in matriz:
        print(i)
    
def escalar(matriz):
    n=int(input("Ingrese el escalar: "))
    for i in matriz:
        for j in range(len(i)):
            i[j]=n*i[j]
    imprimir(matriz)



def main():
    matriz=crear_matriz(filas,columnas)
    imprimir(matriz)
    escalar(matriz)

if __name__=="__main__":
    filas=int(input("Ingrese el numero de filas:"))
    columnas=int(input("Ingrese en numero de columnas:"))
    main()
    