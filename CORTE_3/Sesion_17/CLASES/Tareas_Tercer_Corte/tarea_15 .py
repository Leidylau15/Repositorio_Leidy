# -*- coding: utf-8 -*-
"""Tarea_13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CJiZBnWgBDki-0qI4ybamqdfWe2cGIQi
"""

class Ciudadano:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    # Setters
    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setEdad(self, edad: int):
        self.__edad = edad

    # Getters
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad
     # Métodos
    def bueno(self):
        return f'La persona {self.getNombre()} es un buen ciudadano y tiene {self.getEdad()} años de edad.'

    def Chiste(self):
        return ' dejame contarte un chiste: la policia me detuvo y me dijo:"papeles", le dije: "tijeras, yo gano" y me fui. Creo que quiere una revancha,¡me ha estado persiguiendo durante 45 minutos!.'


class Abogado(Ciudadano):
    def __init__(self, nombre: str, casos_ganados: int, rama_ejercida: str, edad: int):
        super().__init__(nombre, edad)
        self.casos_ganados = casos_ganados
        self.rama_ejercida = rama_ejercida

    # Setters
    def setCasosGanados(self, casos_ganados: int):
        self.casos_ganados = casos_ganados

    def setRamaEjercida(self, rama_ejercida: str):
        self.rama_ejercida = rama_ejercida

    # Getters
    def getCasosGanados(self):
        return self.casos_ganados

    def getRamaEjercida(self):
        return self.rama_ejercida

    # Métodos
    def ley(self):
        return f'La persona {self.getNombre()} ejerce muy bien su profesion, ya que ha ganado {self.getCasosGanados()} casos'

    def Chiste(self):
        return 'Dejame contarte un chiste:En la carcel: Abogado, ¿Cómo va lo mío?, -Bastante bien, pero si puede escaparse mejor.'


class Medico(Ciudadano):
    def __init__(self, nombre: str, especialidad: str, lugar_de_estudios: str, edad: int):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.lugar_de_estudios = lugar_de_estudios

    # Setters
    def setLugarDeEstudios(self, lugar_de_estudios: str):
        self.lugar_de_estudios = lugar_de_estudios

    def setEspecialidad(self, especialidad: str):
        self.especialidad = especialidad

    # Getters
    def getLugarDeEstudios(self):
        return self.lugar_de_estudios

    def getEspecialidad(self):
        return self.especialidad

    # Métodos
    def estudios(self):
        return f'La persona {self.getNombre()} se especializó en {self.getEspecialidad()} y es muy bueno en eso.'

    def Chiste(self):
        return 'Dejame contarte un chiste: Doctor: "Acabo de oir un silbido que no me gusta nada", paciente: "perdone, doctor, es que recien paso su enfermera y no me pude contener.'


class Ingeniero(Ciudadano):
    def __init__(self, nombre: str, edad: int, ingenieria: str, experiencia: int):
        super().__init__(nombre, edad)
        self.__experiencia = experiencia
        self.ingenieria = ingenieria

    #------- Setters--------
    def setExperiencia(self, experiencia: int):
        self.__experiencia = experiencia

    def setIngenieria(self, ingenieria: str):
        self.ingenieria = ingenieria

   #-------  Getters-----------
    def getIngenieria(self):
        return self.ingenieria

    def getExperiencia(self):
        return self.__experiencia

    #------- Métodos
    def empresa(self):
        return f'La persona {self.getNombre()} tiene {self.getExperiencia()} años de experiencia en la empresa Pentagrama S.A.S.'

    def Chiste(self):
        return 'Dejame contarte un chiste: Un optimista ve un vaso medio lleno. Un pesimista ve un vaso medio vacío. Un ingeniero ve un vaso el doble de grande de lo que debería de ser.'


def darChiste(objeto):
    return objeto.Chiste()


def main():
    persona1 = Abogado('Philippi Prietocarrizosa Ferrero ', 12, 'Derecho Penal', 32)
    persona2 = Medico('Salomon Hakin ', 'Pediatra', 'U. Bosque', 28)
    persona3 = Ingeniero('Leidy Laureano', 22, 'Ingenieria mecatronica', 1)
    persona4 = Ciudadano('David Torres', 22)
    personas = [persona1, persona2, persona3, persona4]

    for ciudadano in personas:
        print(f'\nMi nombre es: {ciudadano.getNombre()}, y tengo: {ciudadano.getEdad()}')
        print(darChiste(ciudadano))

if __name__ == "__main__":
    main()