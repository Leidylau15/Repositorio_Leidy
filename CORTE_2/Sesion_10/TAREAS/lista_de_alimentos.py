def canasta():
    f=open('Alimentos.txt','rt')
    line=f.read()
alimentos={'0%':['Arroz','pan','otros productos de panaderia','papa','yuca','otros tuberculos','paltano\n',
                  'cebolla','tomate','zanahorai','revuelto verde','Otras hortalizas y legumbres','frescas\n',
                  'Frijol','Arveja','Otras hortalizas y legumbres secas','narajas','banano','tomate de arobl\n'
                  'Moras','Otras frutas frescas','Res','Cerdo','Pollo','Pescado de mar rio y enlatado','huevos\n',
                  'leche','queso','panela','sal','agua','almuerzo','hambuerguesa','Comidas rapidas calientes\n',
                  'Gastos de cafeteria','Comidas rapidas frias'],
            '5%':['Harina de maiz y otras harinas','Pastas alimenticias','Otros cereales','Carnes frias y embutidos\n',
                  'Azucar','Cafe','Chocolate'],
            '19%':['Cereales preparados','Hortalizas y legumbres enlatadas','Frutas en conserva o secas','Otros productos de mar\n',
                   'Otros derivados lacteos','Aceites','Grasas','Otros condimentos','Sopas y cremas','Salsas y aderezos\n',
                   'Dulces confites y gelatinas','Otros abarrotes']}
def main():
    comida=input('Ingrese un alimento: ')
    if comida=='0%':
        input("Ingrese el costo ")
    print(alimentos[comida])






if __name__=="__main__":
    main()
