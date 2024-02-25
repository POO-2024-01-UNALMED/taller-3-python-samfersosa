class TV:
    numTV = 0

    def __init__(self, marca, estado=False):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setCanal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def getCanal(self):
        return self.canal

    def setVolumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    @classmethod
    def getNumTV(cls):
        return cls.numTV
