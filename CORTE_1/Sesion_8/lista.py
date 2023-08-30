def agregar(milista):
    num=int(input("Que desea agregar: "))
    milista.append(num)
    print(milista)


def main(milista):
    opc="" 
    while opc!="exist":
    
      if opc=="1":
        agregar(milista)
        print("seleccione una opcion:\n",
          "1, Append")
        opc=input("Seleccion: ") 


if __name__=="__main__":
    milista=[2,3,4]
    main(milista)