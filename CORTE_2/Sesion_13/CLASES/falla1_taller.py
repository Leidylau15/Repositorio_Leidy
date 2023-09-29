def lectura():
    f=open("wcm.csv","r",encoding="utf8")
    line=f.readline()
    for  i in line:
        a=i.rstrip('\n').split(',')
        while line !="":
         print(line)
         opc=input('Presione enter')
         line=f.readline()
         print("Finalizo la lectura")
         f.close()
    pass