from Tabla_Hash import *
import random

def opcion0(tabla):
    print("Adios")

def opcion1(tabla):
    for _ in range(1, 20):
        tabla.insertar(int(random.randint(1, 999)))

def opcion2(tabla):
    tabla.print()

def opcion3(tabla):
    print(tabla.printLongitud())

def opcion4(tabla):
    print(f"La cantidad de listas con longitud de hasta 3 es de {tabla.promedioLongitud()}")

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

def switch (opcion, tabla):
    func = switcher.get(opcion, lambda:print("Opcion incorrecta"))
    if opcion == 0 or opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
        func (tabla)
    else:
        func()


if __name__ == '__main__':
    tabla=Tabla_Hash_Encadenada(20)
    band = False
    while not band:
        print("\n-----MENU------")
        print("1 - Insertar")
        print("2 - Print")
        print("3 - Longitud de cada lista de claves sinonimas")
        print("4 - Cantidad de listas con longitud de 3 respecto al promedio")
        print("0 - Salir")
        opcion = int(input("Ingrese una opcion: "))
        switch(opcion,tabla)
        band = int(opcion) == 0