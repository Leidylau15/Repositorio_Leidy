n=float(input("Ingrese la nota"))
#if(n>0  and n<=5):
if(0<=n<=5):
  if n>=3:
    print("Aprobo")
  else: 
    print("Reprobo")
else:
  print("La nota ingresada es invalida")