from re import X
#Ejercicio 1 de la sesion 7
import math as m
import numpy as np
def modulo():
  x=eval(input("Ingrese la coordenada en x:"))
  y=eval(input("Ingrese la coordenada en y:"))
  modulo=m.sqrt((x**2))+((y**2))
  print(f"El modulo del vector {x,y} es: {modulo}")
  com_r=m.degrees(m.atan((y/x)))
  print(f'Sus componentes rectangulares son {modulo, com_r}')




if __name__=="__main__":
  modulo()