festivo={'enero':['1- año nuevo','6-reyes magos'],
         'febrero':['No tiene festivos'],
         'marzo':['20- Dia de san jose']}

def main():
   mes=input('Ingrese un mes: ')
   print(festivo[mes])


if __name__=="__main__":
    main()