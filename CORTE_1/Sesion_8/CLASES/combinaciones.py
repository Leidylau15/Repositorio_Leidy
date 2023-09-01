import fun_factorial as f
def main():
     n=int(input("Ingrese un numero de elementos :"))
     m=int(input("Ingrese el numero de grupos:"))
     cmb=(f(n)/(f(m)*(f(n-m))))
     print(f"El numero de combinaciones es {cmb}")







if __name__=="__main__":
    main()