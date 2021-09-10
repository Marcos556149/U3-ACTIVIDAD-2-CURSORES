class Nodo:
    __dato = 0
    __sig = 0
    def __init__(self):
        self.__sig = -2 #Equivale a null
    def setDato(self,dato):
        self.__dato = dato
    def getDato(self):
        return self.__dato
    def setSig(self,sig):
        self.__sig = sig
    def getSig(self):
        return self.__sig
