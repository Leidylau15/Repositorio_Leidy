class  Imc:
     def __init__(self) -> None:
          self.nombre=None
          self.apellido=None
          self.estatura=None        #Constructor 
          self.peso=None

     def metodoCalculo(Self):
        def calcular_imc(altura, peso):
         alt = altura / 100
         imc = peso / (alt ** 2)
        return Imc

     def obtener_escala(imc):
       if imc < 18.5:
        return "Bajo peso"
       elif imc < 24.9:
        return "Peso normal"
       elif imc < 29.9:
        return "Sobrepeso"
       else:
        return "Obesidad"




def main():
     persona1 = Imc()
     persona1.nombre='Pedro'
     persona1.apellido='Caceres'
     persona1.estatura='188 cm '
     persona1.peso='97 kg '

     persona2 = Imc()
     persona2.nombre='Maria'
     persona2.apellido='Perez'
     persona2.estatura='160 cm '
     persona2.peso='47 kg' 

     persona3 = Imc()
     persona3.nombre='Julian'
     persona3.apellido='Dominguez'
     persona3.estatura='158 cm '
     persona3.peso='58 kg'

     persona4 = Imc()
     persona4.nombre='Jessica'
     persona4.apellido='Fuentes'
     persona4.estatura='170 cm '
     persona4.peso='73 kg'

     





if __name__=="__main__":
     main()