def cuenta_atras(num):
    num-=1
    if num>0:
        print(num)
        cuenta_atras(num)
    else:
        print("BooooM!")
        print("Fin de la funcion", num)
if __name__=="__main__":
    cuenta_atras(6)