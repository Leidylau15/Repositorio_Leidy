import Fcn_externa
import fun3

def main():
    nombre=input("Ingrese su nombre:")
    surname=input("Ingr4ese su apellido:")
    print("------------------")
    Fcn_externa.matrix(nombre,surname)
    print("------------------")
    print(f"Ejecutado desde {__name__}")
    print("**************")
    fun3.suma()
    print("**************")


if __name__=="__name__":
    main()