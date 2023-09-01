
def conteo(num):
    if num>0:
        num-=1
        print(num)
        conteo(num)
    print(num)







if __name__=="__name__":
    n=int(input("Hasta que numero desea contar:"))
    conteo(n)