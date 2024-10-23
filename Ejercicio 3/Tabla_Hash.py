from classNodo import *
import numpy as np

class Tabla_Hash_Encadenada:
    __tamanio : int
    __tabla : np.ndarray
    def __init__(self, xtamaño):
        self.__tamanio = int(xtamaño / 0.7)
        self.__tabla = np.ndarray(self.__tamanio, dtype=object)


    def hash(self,clave):
        acumulador = 0
        factor = 1000 #Cantidad de pliegues 3
        while clave > 0:  
            acumulador += clave % factor  
            clave //= factor  
        return acumulador % self.__tamanio

    
    def insertar(self, clave):
        indice = self.hash(clave)
        nodo = Nodo(clave)
        if self.__tabla[indice] is None:
            self.__tabla[indice] = nodo
        else:
            aux = self.__tabla[indice]
            while aux.getSig() is not None:
                aux = aux.getSig()
            aux.setSig(nodo)
    

    def longitud(self):
        longitudes = []
        for i in range(len(self.__tabla)):
            contador = 0
            nodo = self.__tabla[i]
            while nodo is not None:
                contador+=1
                nodo = nodo.getSig()
            longitudes.append(contador)
        return longitudes

    def printLongitud(self):
        longitudes = self.longitud()
        for i in range(len(longitudes)):
            print(f"Indice {i+1} longitud de la lista es de {longitudes[i]}")

    def promedioLongitud(self):
        longitudes = self.longitud()
        if len(longitudes) == 0:
            print("Lista vacia")
        else:
            promdio = sum(longitudes) / len(longitudes)
            contador = 0
            for longitud in longitudes:
                if abs(longitud - promdio) <= 3:
                    contador+=1
            return contador

    def print(self):
        # Imprimimos la tabla hash y las listas vinculadas en cada índice
        for i in range(self.__tamanio):
            print(f"Índice {i}:", end=" ")
            nodo = self.__tabla[i]
            if nodo is None:
                print("None")
            else:
                # Recorremos e imprimimos la lista vinculada
                while nodo:
                    print(f"[Clave: {nodo.getClave()}] ->", end=" ")
                    nodo = nodo.getSig()
                print("None")