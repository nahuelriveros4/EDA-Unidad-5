from tabla_hash import *


def opcion0(tabla1):
    print("Adios")

def opcion1(tabla1):
    tabla1.insertar('clave123')
    tabla1.print()

switcher = {
    0: opcion0,
    1: opcion1
}

def switch (opcion, tabla1):
    func = switcher.get(opcion, lambda:print("Opcion incorrecta"))
    if opcion == 0 or opcion == 1:
        func (tabla1)
    else:
        func()


if __name__ == '__main__':
    tabla1 = tabla_hash()
    band = False
    while not band:
        print("\n-----MENU------")
        print("1 - Tabla")
        print("0 - Salir")
        opcion = int(input("Ingrese una opcion: "))
        switch(opcion,tabla1)
        band = int(opcion) == 0