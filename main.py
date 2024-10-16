from tabla_hash import *


def opcion0(tabla1,tabla2):
    print("Adios")

def opcion1(tabla1,tabla2):
    for _ in range(1, 20):
        tabla2.insertar(int(random.randint(1, 999)))
    tabla2.print()

def opcion2(tabla1, tabla2):
    for _ in range(1, 20):
        tabla1.insertar(int(random.randint(1, 999)))
    tabla1.print()

def opcion3(tabla1,tabla2):
    op = int(input("Buscar en tabla 1 (No Prima) o 2 (Prima): "))
    if op == 1:
        clave = int(input("Ingrese la clave a buscar: "))
        tabla2.buscar(clave)
    else:
        clave = int(input("Ingrese la clave a buscar: "))
        tabla1.buscar(clave)


switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch (opcion, tabla1, tabla2):
    func = switcher.get(opcion, lambda:print("Opcion incorrecta"))
    if opcion == 0 or opcion == 1 or opcion == 2 or opcion == 3:
        func (tabla1,tabla2)
    else:
        func()


if __name__ == '__main__':
    tabla1 = tabla_hash(True)
    tabla2 = tabla_hash(False)
    band = False
    while not band:
        print("\n-----MENU------")
        print("1 - Tabla No Prima")
        print("2 - Tabla Prima")
        print("3 - Buscar")
        print("0 - Salir")
        opcion = int(input("Ingrese una opcion: "))
        switch(opcion,tabla1, tabla2)
        band = int(opcion) == 0