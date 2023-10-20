class Ciudadano:
    def __init__(self):
        self.__nombre = None
        self.__cedula = None
        self.__edad = None

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_cedula(self, cedula):
       if 8 <= len(cedula) <= 10:
            self.__cedula = cedula
       else:
            print("La cédula debe tener entre 8 y 10 dígitos.")

    def get_cedula(self):
        return self.__cedula

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo mayor que cero.")


    def get_edad(self):
        return self.__edad

    def mostrar(self):
        print('-------Ciudadanos -----\n')
        print(f'Nombre: {self.__nombre},\n '
              f'Edad: {self.__edad},\n '
              f'CC: {self.__cedula}')


    def es_mayor_de_edad(self):
      if self.__edad >= 18:
       print('La persona es mayor de edad')
      else:
        print(f"La persona es menor de edad")
     
   

def main():
    personas = []
    opc = 'y'

    while opc != 'n':
        persona = Ciudadano()
        persona.set_nombre(input('Nombre: '))
        persona.set_cedula(input('Ingrese su cédula: '))
        edad = int(input('Ingrese su Edad: '))
        persona.set_edad(edad)
        personas.append(persona)
        opc = input('¿Desea agregar otra persona? (y/n): ')

    for i in personas:
        i.mostrar()
        i.es_mayor_de_edad()


if __name__ == "__main__":
    main()


