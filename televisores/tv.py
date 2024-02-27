class TV:
    numTV = 0

    @classmethod
    def setNumTV(cls, num):
        cls.numTV = num
    @classmethod
    def getNumTV(cls):
        return cls.numTV

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1
        self.__precio = 500
        self.__volumen = 1
        self.__control = None
        TV.numTV += 1

    def setCanal(self, canal):
        if self.__estado and 1 <= canal <= 120:
            self.__canal = canal

    def setPrecio(self, precio):
        self.__precio = precio

    def setVolumen(self, volumen):
        if self.__estado and 0 <= volumen <= 7:
            self.__volumen = volumen

    def getMarca(self):
        return self.__marca

    def getCanal(self):
        return self.__canal

    def getPrecio(self):
        return self.__precio

    def getEstado(self):
        return self.__estado

    def getVolumen(self):
        return self.__volumen

    def getControl(self):
        return self.__control

    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def canalUp(self):
        if self.__estado and 1<=self.__canal < 120:
            self.__canal += 1

    def canalDown(self):
        if self.__estado and 1<self.__canal<=120:
            self.__canal -= 1

    def volumenUp(self):
        if self.__estado and 0<=self.__volumen < 7:
            self.__volumen += 1

    def volumenDown(self):
        if self.__estado and 0<self.__volumen<=7:
            self.__volumen -= 1

    def setControl(self, control):
        self.__control = control
    
    def setMarca(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca
