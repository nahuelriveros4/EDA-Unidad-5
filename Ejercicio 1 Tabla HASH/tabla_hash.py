import numpy as np
import random
class tabla_hash:
    __lista: np.ndarray
    def __init__(self,primoo ,N = 20):
        if primoo:
            self.__M = self.primo(int(N / 0.7)) 
        else:
            self.__M = int(N / 0.7)
        self.__lista = np.ndarray(self.__M,dtype=object)
        self.__lista.fill(None) 

    def primo(self,x):
        for i in range(2,x):
            if x % i == 0:
                return self.primo(x+1)
        return x

    def hash(self,clave):
        return int(clave) % self.__M 
    
    def insertar(self,clave):
        cont = 1
        direccion = self.hash(clave)
        while self.__lista[direccion] is not None and cont != self.__M:
            cont+=1
            direccion = (direccion+1) % self.__M
        if cont != self.__M:
            self.__lista[direccion] = clave
            print(f"{self.__lista[direccion]} Comparaciones que ocupó: {cont}")
        else:
            print("Tabla llena")

    def buscar(self, clave):
        print("Buscando")
        direccion = self.hash(clave)
        cont = 1
        while self.__lista[direccion] is not None and cont <= self.__M:
            if self.__lista[direccion] == clave:
                print(f"Clave {clave} encontrada en la posición {direccion} después de {cont} comparaciones")
                return
            else:
                direccion = (direccion + 1) % self.__M
                cont += 1
        print(f"Clave {clave} no encontrada en la tabla después de {cont - 1} comparaciones.")

    def print(self):
        for i in range(len(self.__lista)):
            print(f"Clave: {self.__lista[i]} ///  Direccion: {i}")