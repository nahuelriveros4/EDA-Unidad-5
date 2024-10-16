import numpy as np
import random
class tabla_hash:
    __lista: np.array
    def __init__(self,N = 33):
        self.__M = N
        self.__lista = np.ndarray(self.__M,dtype=object)
        self.__lista.fill(None) 

    
    def metodo_division(self, clave):
        return int(clave) % self.__M
    
    def metodo_extraccion(self,clave):
        inicio=2
        extraccion_pura= int(str(clave)[inicio:inicio+len(str(self.__M))]) 
        return extraccion_pura % self.__M 
    
    def plegado(self,clave):
        num_pliegues= 3
        j=0
        direccion=0
        for i in range(num_pliegues):
            hasta=int(len(str(clave)) * ((i+1)/num_pliegues)) 
            print(int(str(clave)[j : hasta]))
            direccion+= int(str(clave)[j : hasta])
            j= hasta
        return direccion % self.__M

    def cuadrado_medio(self,clave):
        cuadrado= str(clave ** 2)
        desde= int(len(cuadrado)/2) - 1 
        direccion= int(cuadrado[desde:desde+2]) 
        return direccion % self.__M

    def metodo_alfanumerico(self, clave):
        clave= str(clave)
        direccion=0
        for i in range(len(clave)):
            direccion+= ord(clave[i]) * (10**(i+1)) 
        return direccion  % self.__M

    
    def insertar(self,clave):
        cont = 1
        direccion = self.metodo_alfanumerico(clave)
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