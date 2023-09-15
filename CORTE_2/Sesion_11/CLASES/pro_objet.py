class  estudiante:
     def __init__(self) -> None:
          self.nombre=None
          self.apellido=None        #Constructor 
          self.edad=None
          self.nacionalidad='Colombia'
    
def main():
     est1=estudiante()     #Instancia 
     est1.nombre='Juan'      #apuntador est1.nombre 
     est1.apellido='Picon'   # objeto 1 
     est1.edad='17'

     est2=estudiante()
     est2.nombre='Roger'
     est2.apellido='Piñeros'   # objeto 2 
     est2.edad='17'

     print(f' el estudiante: {est1.nombre} {est1.apellido}',\
           f'tiene una edad de: {est1.edad}',\
           f'y su nacionalidad es: {est1.nacionalidad}')







if __name__=="__main__":
    main()
