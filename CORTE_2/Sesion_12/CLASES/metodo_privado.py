class  Estudiante:
     def __init__(self) -> None:
          self.__nombre=None
          self.__apellido=None        #Constructor 
          self.__edad=None
          self.nacionalidad='Colombia'

     def setNombre(self,nombre:str):
         self.__nombre=nombre
     def getNombre(self):
         return self.__nombre
     
     def setApellido(self,apellido:str):
         self.__apellido=apellido
     def getApellido(self):
         return self.__apellido
     
     def setEdad(self,edad:str):
         if int(edad) >21:
           self.__edad=edad
         else:
             self.__edad="Menor de edad"
     def getEdad(self):
         return self.__edad
     
     

     def entender(self):
      return 'Si, aprendi mucho hoy :)' 
     
     def __licor(self):
         edad=self.__edad
         if int(edad)>21:
             return "puede beber una pola!"
         else: 
             return"le toco jugo!"
     def getlicor(self):
      return self.__licor()
     
    
def main():
     estudiante=[]
     opc='n'
     while 1:
         est=Estudiante()
         est.setNombre(input("Nombre: "))
         est.setApellido(input("Apellido: "))
         est.setEdad(int(input("Edad: ")))
         opc=input("desea salir? (y/n)")
         if opc=="y":
             break
         else:
             print("invalido")
     print(f'------------Clase 2023-II----------\n')        
     for i in estudiante:
         print(f'nombre: {i.getNombre()} {i.getApellido()}\n\
              Edad: {i.getEdad()}\n')
         print(est.getlicor())


if __name__=="__main__":
    main()