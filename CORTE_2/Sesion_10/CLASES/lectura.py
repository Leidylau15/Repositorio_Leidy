def lectura():
    f=open("matrizAsignacion.txt","rt")
    line=f.readlines()
    for  i in line:
        a=i.rstrip('\n').split(',')
        print(f'{a}=>{int(a[0])+int(a[1])}')
        





















if __name__=="__main__":
    lectura()
