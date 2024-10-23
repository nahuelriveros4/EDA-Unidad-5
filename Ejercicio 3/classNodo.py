class Nodo:
    __clave: int
    __sig: object
    def __init__(self, xclave):
        self.__clave = xclave
        self.__sig = None

    def getClave(self):
        return self.__clave
    
    def setSig(self, xsig):
        self.__sig = xsig

    def getSig(self):
        return self.__sig