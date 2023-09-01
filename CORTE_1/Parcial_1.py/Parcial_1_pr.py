import random as rd 
def rates():
    comision=rd.randint(10,50)
def menu():
    print("Que desea hacer:\n"\
      "1. Conversion de COP a cualquier divisa\n 2. Tasas de cambio y su comision.")
    
    
 
def main():
    s=menu()
    comision=rates()
    s=input("Ingrese la opcion a realizar:")
    if (s.lower()=="1"):
        print("USD,EUR,CNY,JPY,PEN")
        div=input("A divisa desea hacer el cmabio:")
        din=input("Cuanto COP desea cambiar")
        if (div.lower()=="USD"):
            USD:4108
            Pecio_venta=(din*USD+{comision})
        elif (div.lower()=="EUR"):
            EUR=4454
            Pecio_venta=(din*EUR+{comision})
        elif (div.lower()=="CNY"):
            CNY=563
            Pecio_venta=(din*CNY+{comision})
        elif (div.lower()=="JPY"):
            JPY=28
            Pecio_venta=(din*JPY+{comision})
        elif (div.lower()=="PEN"):
            PEN=4454
            Pecio_venta=(din*PEN+{comision}) 
        else:
            print("Divisa invalida ")  
    elif (s.lower()=="2"):
        print(f"Divisa; USD, Tasa: 4108, comision:{comision}'n"\
               f"Divisa; EUR, Tasa: 4454, comision:{comision}'n"\
                 f"Divisa; CNY, Tasa: 563, comision:{comision}'n"\
                  f"Divisa; JPY, Tasa: 28, comision:{comision}'n"\
                f"Divisa; PEN, Tasa: 1106, comision:{comision}")
    else:
      print("Seleccion invalida")


 

    




    


if __name__=="__main__":
    main()

