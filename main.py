from funciones import menu, menu_option, lista, borarterminal
from lecto_escritura import  fecha_creacion , leer_archivo

if __name__ == "__main__":
    leer_archivo()


    while True:
        lista_codigos = lista()
        borarterminal()
        print("=" * 50)
        fecha_creacion()
        menu()
        option = int(input("Ingrese la opcion:\n"))
        menu_option(option, lista_codigos)


