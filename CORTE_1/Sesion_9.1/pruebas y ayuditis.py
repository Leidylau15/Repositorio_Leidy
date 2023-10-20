# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:43:44 2023

@author: casa
"""

# Datos en una cadena de texto (cada línea representa una fila)
data_str = """home_team,away_team,home_score,home_penalty,away_score,away_penalty,home_manager,home_captain,away_manager,away_captain,Attendance,Venue,Round,Date,Referee,Host,Year
Argentina,France,3,4,3,2,LionelÂ Scaloni,LionelÂ Messi,DidierÂ Deschamps,HugoÂ Lloris,88966,Lusail Iconic Stadium- Lusail,Final,44913,Szymon Marciniak,Qatar,2022
Croatia,Morocco,2,,1,,ZlatkoÂ DaliÄ‡,LukaÂ ModriÄ‡,HoalidÂ Regragui,HakimÂ Ziyech,44137,Khalifa International Stadium- Doha,Third-place match,44912,Abdulrahman Ibrahim Al Jassim,Qatar,2022
France,Morocco,2,,0,,DidierÂ Deschamps,HugoÂ Lloris,HoalidÂ Regragui,RomainÂ SaÃ¯ss,68294,Al Bayt Stadium- Al Khor,Semi-finals,44909,CÃ©sar Arturo Ramos,Qatar,2022
Argentina,Croatia,3,,0,,LionelÂ Scaloni,LionelÂ Messi,ZlatkoÂ DaliÄ‡,LukaÂ ModriÄ‡,88966,Lusail Iconic Stadium- Lusail,Semi-finals,44908,Daniele Orsato,Qatar,2022
Morocco,Portugal,1,,0,,HoalidÂ Regragui,RomainÂ SaÃ¯ss,FernandoÂ Santos,Pepe,44198,Al Thumama Stadium- ath-ThumÄma,Quarter-finals,44905,Facundo Tello,Qatar,2022
England,France,1,,2,,GarethÂ Southgate,HarryÂ Kane,DidierÂ Deschamps,HugoÂ Lloris,68895,Al Bayt Stadium- Al Khor,Quarter-finals,44905,Wilton Sampaio,Qatar,2022
Croatia,Brazil,1,4,1,2,ZlatkoÂ DaliÄ‡,LukaÂ ModriÄ‡,Tite,ThiagoÂ Silva,43893,Education City Stadium- Doha,Quarter-finals,44904,Michael Oliver,Qatar,2022
Netherlands,Argentina,2,3,2,4,LouisÂ vanÂ Gaal,VirgilÂ vanÂ Dijk,LionelÂ Scaloni,LionelÂ Messi,88235,Lusail Iconic Stadium- Lusail,Quarter-finals,44904,Antonio MatÃ©u,Qatar,2022
Morocco,Spain,0,3,0,0,HoalidÂ Regragui,RomainÂ SaÃ¯ss,LuisÂ Enrique,SergioÂ Busquets,44667,Education City Stadium- Doha,Round of 16,44901,Fernando Rapallini,Qatar,2022
Portugal,Switzerland,6,,1,,FernandoÂ Santos,Pepe,MuratÂ Yakin,GranitÂ Xhaka,83720,Lusail Iconic Stadium- Lusail,Round of 16,44901,CÃ©sar Arturo Ramos,Qatar,2022
Japan,Croatia,1,1,1,3,HajimeÂ Moriyasu,MayaÂ Yoshida,ZlatkoÂ DaliÄ‡,LukaÂ ModriÄ‡,42523,Al Janoub Stadium- Al Wakrah,Round of 16,44900,Ismail Elfath,Qatar,2022
Brazil,Korea Republic,4,,1,,Tite,ThiagoÂ Silva,PauloÂ Bento,SonÂ Heung-min,43847,Stadium 974- Doha,Round of 16,44900,ClÃ©ment Turpin,Qatar,2022
"""

# Dividir las líneas para obtener las filas
filas = data_str.strip().split('\n')

# Inicializar una matriz vacía para almacenar los datos
matriz = []

# Dividir cada fila en elementos utilizando ',' como separador y agregarlos a la matriz
for fila in filas:
    elementos = fila.split(',')
    matriz.append(elementos)

# Imprimir la matriz resultante
for fila in matriz:
    print(fila)
def contar_participaciones(data):
    participaciones_por_pais = {}  # Diccionario para almacenar las participaciones por país

    for fila in data[1:]:  # Excluir la primera fila que contiene los encabezados
        home_team, away_team, year = fila[0], fila[1], fila[-1]

        # Contar las participaciones del equipo de casa
        if home_team in participaciones_por_pais:
            participaciones_por_pais[home_team].append(year)
        else:
            participaciones_por_pais[home_team] = [year]

        # Contar las participaciones del equipo visitante
        if away_team in participaciones_por_pais:
            participaciones_por_pais[away_team].append(year)
        else:
            participaciones_por_pais[away_team] = [year]

    # Calcular el número total de participaciones por país
    total_participaciones_por_pais = {}
    for pais, participaciones in participaciones_por_pais.items():
        total_participaciones = len(set(participaciones))  # Utiliza un conjunto para eliminar duplicados
        total_participaciones_por_pais[pais] = total_participaciones

    return total_participaciones_por_pais

# Llamar a la función con la matriz de datos
total_participaciones = contar_participaciones(matriz)

# Imprimir el resultado
for pais, participaciones in total_participaciones.items():
    print(f"{pais}: {participaciones} participaciones en la Copa del Mundo")
