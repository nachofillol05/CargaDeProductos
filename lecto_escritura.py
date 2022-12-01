import os.path, time


# productos
def leer_archivo(filename="productos.txt"):
    try:
        with open(filename, "r") as f:
            lista_productos = f.readlines()
        return lista_productos
    except FileNotFoundError:
        print(f"No existe el archivo {filename}")


def escribir_archivo(linea, filename="productos.txt", modo="a"):
    with open(filename, modo) as f:
        f.write(linea)


def fecha_creacion():
    fecha = time.ctime(os.path.getctime("productos.txt"))
    print("archivo creado en la fecha : %s" % time.ctime(os.path.getctime("productos.txt")))


# clientes

def leer_archivocli(filename="clientes.txt"):
    try:
        with open(filename, "r") as f:
            lista_clientes = f.readlines()
        return lista_clientes
    except FileNotFoundError:
        print(f"No existe el archivo {filename}")


def escribir_archivocli(clientes, filename="clientes.txt", modo="a"):
    with open(filename, modo) as f:
        f.write(clientes)


def fecha_creacioncli():
    print("archivo creado en la fecha : %s" % time.ctime(os.path.getctime("clientes.txt")))


# lista
def escribir_lista(comprador, filename="lista.txt", modo="a"):
    with open(filename, modo) as f:
        f.write("\n")
        f.write(comprador)


def escribir_lista2(codigo, filename="lista.txt", modo="a"):
    with open(filename, modo) as f:
        f.write(" : ")
        f.write(codigo)
