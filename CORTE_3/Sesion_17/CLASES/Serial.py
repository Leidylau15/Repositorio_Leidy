#Uso de la libreria pyseruial 
#para instalar  ejecutar -m pip install pyserial
import serial


puerto=serial.Serial("COM4", baudrate=9600, timeout=1)
while 1:
    dato=input("Dato a enviar") 
    puerto.write(dato.encode('utf_8'))
    time.sleep(0.5)
    line=puerto.readline()
    print(line)
    time.sleep(0.5)











