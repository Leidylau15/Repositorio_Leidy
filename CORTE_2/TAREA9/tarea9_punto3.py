# -*- coding: utf-8 -*-
"""Tarea9_punto3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NerPGAlJGdSpUiZ4pe_AN_j_XI2K0OMK
"""

#punto 3
def posiciones(a, b):
    posic = []
    for i in range(len(a)):
        if a[i] == b:
            posic.append(i)
    return posic

def main():
    a = str(input('Ingrese una palabra: '))
    b = str(input('Ingrese una letra de esa palabra: '))
    posic = posiciones(a, b)

    if not posic:
        print(f"la letra '{b}' no se encuentra en la palabra '{a}'")
    else:
        print(f"Las posiciones de '{b}' en '{a}' son: {posic}")

if __name__ == "__main__":
    main()