import linecache
import os
import time
from lecto_escritura import escribir_archivo, fecha_creacion, escribir_lista, escribir_lista2


def menu():
    print("=" * 50)
    print("Bienvenido a el contador de productos vendidos")
    print("=" * 50)
    print("1. Cargar codigo del producto")
    print("2. Ver productos vendidos")
    print("3. Ver clientes")
    print("4. lista de productos")
    print("5. ganancias totales")
    print("6. agregar nuevo producto")
    print("7. borrar los datos")
    print("8. Salir")
    print("=" * 50)


def borarterminal():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def menu_option(option: int, *args):
    if option > 8 or option < 1:
        print("=" * 50)
        print(f"La opcion {option} no esta en el rango de opciones\n")
        print("=" * 50)
    else:

        dict_menu = {
            1: cargar_codigo_producto,
            2: ver_productos_vendidos,
            3: clientes,
            4: listam,
            5: ganancias,
            6: productonuevo,
            7: borrar,
            8: salir,

        }

        dict_menu[option](*args)
        input("Presione ENTER para continuar")


def cargar_codigo_producto(lista_codigos, *args):
    print("Estas en la carga de productos")
    print("=" * 50)
    productos = str(input("Ingrese el nombre del producto\n"))
    print("=" * 50)
    with open("lista.txt", "r") as d:
        lista = d.read()
    if productos not in lista:
        print(f"ingrese un nombre valido porfavor (consultar lista)\n", "".join(lista))
    else:
        escribir_archivo(f"{productos} la fecha que lo vendio: {time.strftime('%d/%m/%y')}\n")
        cliente = str(input("¿a quien se lo vendio?\n"))
        with open("clientes.txt", "r") as f:
            losclientes = f.read()
        if cliente not in losclientes:
            with open("clientes.txt", "a+")as c:
                c.write(f"{cliente}\n")
        else:
            print("ya cargo ese cliente por lo que no sera cargado de nuevo")

    print("=" * 50)


def salir(*args):
    print("Termino la ejecucion")
    exit()


def ver_productos_vendidos(lista_codigos, *args):
    print("=" * 50)
    with open(r"productos.txt", 'r') as b:
        productos = b.read()
    print("=" * 50)
    if productos == "":
        print("todavia no vendio nada")
    else:
        print("Aca te muestro productos vendidos")
        for elemento in lista_codigos:
            nombre, _ = obtener_nombre_precio(elemento)
            cod_count = productos.count(nombre)
            print(nombre, cod_count)
        print("=" * 50)


def productonuevo(lista_codigos, *args):
    producto = input("escriba el nuevo producto, sin espacios\n")
    precio_producto = input(f"precio del producto {producto}\n")
    producto_nuevo = f"{producto} : {precio_producto}"
    lista_codigos.append(producto_nuevo)
    with open(r"lista.txt", "a") as d:
        d.write(f"\n{producto_nuevo}")

    print(
        f"el producto que agrego fue {producto} y tiene un valor de {precio_producto}")


def clientes(*args):
    b = open(r"clientes.txt", 'r')
    listaclientes = b.read()
    if listaclientes == "":
        print("no ha vendido a nadie todavia")
    else:
        print(listaclientes)
    b.close()


def borrar(*args):
    confirmacion = input("esta seguro que desea borrar el archivo,se eliminaran todos los datos, escriba si o no\n")
    confirmacion = confirmacion == "si"
    if confirmacion:
        f = open("productos.txt", "r+")
        f.truncate(0)
        a = open("clientes.txt", "r+")
        a.truncate(0)
        b = open("lista.txt", "r+")
        b.truncate(0)
        b.close()
        a.close()
        f.close()
        exit()
    else:
        pass


def obtener_nombre_precio(elemento, *args):
    producto = elemento.replace(" ", "").split(":")
    nombre = producto[0]
    precio = producto[1].replace("\n", "")
    return nombre, precio


def listam(lista_codigos, *args):
    for elemento in lista_codigos:
        nombre, precio = obtener_nombre_precio(elemento)
        print(f"{nombre}, con un precio de ${precio} ")


def lista(*args):
    print("producto : precio")
    with open("lista.txt", "r") as d:
        lista = d.readlines()
        print("".join(lista))

    return lista


def print_lista(*args):
    print("".join(lista()))


def ganancias(lista_codigos, *args):
    total = 0
    with open(r'productos.txt', 'r') as b:
        productos = b.read()
    print("=" * 50)
    lista_codigos = lista()
    for elemento in lista_codigos:
        nombre, precio = obtener_nombre_precio(elemento)
        cod_count = productos.count(nombre)
        if cod_count != 0:
            total += cod_count * int(precio)
            print(f"del producto {nombre}, vendio {cod_count}, a un precio de {precio}")
        else:
            print(f"del producto {nombre}, no vendio ninguno")
    print(f"el total ganado es {total}")
    print("=" * 50)


if __name__ == "__main__":
    print("hola")
