def lectura():
    f = open("wcm.csv", "r", encoding="utf8")
    line = f.readline()
    if line:
        a = line.rstrip('\n').split(',')
        print(a)
    f.close()

def campeon_mundial(listado):
    campeones={}
    for partidos in listado:
      if partidos[12]=='Final':
         
         if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
            if partidos[0] not in campeones:
               campeones[partidos[0]]=[partidos[16]]
            else:
               list_year=campeones[partidos[0]]
               list_year.append(partidos[16])
               campeones[partidos[0]]=list_year
         else:
            if partidos[1] not in campeones:
               campeones[partidos[1]]=[partidos[16]]

           # print(f'ganador es: {partidos[0]}')
            else:
            #print(f'ganaodr es: {partidos[1]}')
               list_year=campeones[partidos[1]]
               list_year.append(partidos[16])
               campeones[partidos[1]]=list_year
    campeones=dict(sorted(campeones.items()))
    print('\n--------------------------Listado de campeones mundiales--------------------\n')
    for pais,year in campeones.items():
       print(f'{pais}:campeon en {year}')
    pais=input('ingrese un pais:')
    if pais in campeones:
     year=campeones[pais]
     print(f'fue campeon en los años {year}')
    else:
       print(f'{pais} no ha sido campeon del mundo ')


def main():

    print('selecciones una de las siguietnes opciones: \n'\
         '1. cantidad de mundiales ganados por un pais\n'\
            '2. cantidad de subcampeones por un pais')
    listado=lectura()
   #print(listado[0])

    menu={'1':campeon_mundial,}
    opcion=input('seleccione una opcion')

    if opcion in menu:
      menu[opcion](listado)
    else:
      print('opcion invalida')
