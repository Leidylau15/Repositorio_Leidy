class  Estudiante:
     def __init__(self) -> None:
          self.nombre=None
          self.apellido=None        #Constructor 
          self.edad=None
          self.nacionalidad='Colombia'

     def entender(self):
      return 'Si, aprendi mucho hoy :)' 
     

def main():
    estudiante=[]
    while 1:
        est=Estudiante()
        est.nombre=input('Nombre: ')
        est.apellido=input('apellido: ')
        est.edad=input('edad: ')
        estudiante.apppend(est)
        opc=input('Desea sali?: (y/n)' )
        if opc=='y':
            break 
        else:
            print('Invalido')
    print(f'------------Clase 2023-II----------\n')        
    for i in estudiante:
        print(f'nombre: {i.nombre} {i.apellido}\n\
              Edad: {i.edad}\n\n')
        
    




if __name__=="__main__":
    main()
