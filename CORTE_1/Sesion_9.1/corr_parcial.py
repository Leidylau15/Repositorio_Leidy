from random import uniform as u
def rates():
    comision=[]
    for i in range(5):
        comision.append(round(u(0.1,0.5),2))
    return comision

def ver_tasas(comision,divisas,cambios):
    for i in range(5):
        print(f"divisa: {divisas[i]}, tasa: {cambios[i]}, comision: {comision[i]}")

def conversion(comision, divisas,cambio):
    div=input("A que divisa desea hacer el cmabio: ").upper()
    if div in divisas:
        idx=div.index(divisas)
        divisas=(divisas[idx])
        comision=(comision[idx])
        tasa=int(cambio[idx])
        precio_venta=tasa+(tasa*comision)
        cambio=int(input("Que valor desea cambir: "))
        total=cambio//precio_venta #parte entera de una division 25.55 a 25 
        vueltas=(round (cambio-precio_venta*total),2)
        print(f"Cambio: {total} {divisas}, Devolucion: {vueltas} COP")
        return 1 
    print("Ingrese un valor valido\n")


           

def menu():
    comsion=rates()
    divisas=["USD","EUR","CNY","JPY","PEN"]
    cambios=["4108","4454","563","28","1106"]

    print( "1. Conversion de COP a cualquier divisa\n",'2. Tasas de cambio y su comision.', "3. Salir")   
    ocp=input("Seleccione una opcion:")

    while opc!="Salir":
        if opc=="1":
            conversion(comsion, divisas,cambios)
        elif opc=="2":
            ver_tasas()
        elif opc=="Salir":
            break
        else: 
            print("Seleccion invalida")
        print("1. Conversion de COP a cualquier divisa\n",'2. Tasas de cambio y su comision.',"3. Salir")
        opc=input("Seleccione una opcion:")
        


def inicio():
    menu()
    
    



if __name__=="__main__":
    inicio()