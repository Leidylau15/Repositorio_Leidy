class Deportista():
    def __init__(self,nombre:str, edad:int,documento:str):
        self.__nombre=nombre
        self.__edad=edad
        self.__documento=documento

    def setNombre(self,nombre:str):
         self.__nombre=nombre

    def getNombre(self):
         return self.__nombre
    
    def setEdad(self,edad:int):
         self.__edad=edad

    def getEdad(self):
         return self.__edad
    
    def setDocumento(self,documento:str):
         self.__documento=documento
         
    def getDocumento(self):
         return self.__documento
    def jugador(self):
        return super
  
  
class Futbloista(Deportista):
     def __init__(self, nombre: str, edad: int, documento: str,nombre_equipo:str,goles:int):
          super().__init__(nombre, edad, documento)
          self.nombre_equipo=nombre_equipo
          self.goles=goles
    #--------------setters------------------
     def setNombreEquipo(self,nombre_equipo:str):
          self.nombre_equipo=nombre_equipo
     def setGoles(self,goles:int):
          self.goles=goles
    #--------------getters------------------
     def getNombreEquipo(self):
      return self.nombre_equipo
     def getGoles(self):
         return self.goles
     #--------------metodos------------------
     def patear(self):
         return f'el jugador {self.getNombre()} acaba de anotar un gol'

class tenista(Deportista):
     def __init__(self, nombre: str, edad: int, documento: str, set_ganados:int,ace:int):
          super().__init__(nombre, edad, documento)
          self.set_ganados=set_ganados
          self.ace=ace

     #--------------setters------------------
     def setSetGanados(self,set_ganoados:int):
          self.set_ganoados=set_ganoados
     def setAce(self,ace:int):
          self.ace=ace
    #--------------getters------------------
     def get(self):
      return self.set_ganoados
     def getGoles(self):
         return self.ace
     #--------------metodos------------------
     def Ace(self):
         return f'El jugador {self.getNombre()} acaba de hacer un punto'

     


def main():
    jugador1=Futbloista('Radamel Falcao Garcia',\
    35,'21234556', 'Colombia',34)
    jugador2=tenista('roger federer',42,'234567898',6,12,)
    jugador3=Deportista('Magnus Carlsen',32,'1234566789')
    print(jugador2.Ace())
    print(jugador1.patear())
    print(f'el jugador {jugador3.jugador()} aes un maestro ajedrecista')




if __name__=="__main__":
    main()