class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1
        self.__volumen = 1
        self.__precio = 500
        self.__control = None
        TV.numTV += 1

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_estado(self):
        return self.__estado

    def turn_on(self):
        self.__estado = True

    def turn_off(self):
        self.__estado = False

    def canal_up(self):
        if self.__estado and self.__canal < 120:
            self.__canal += 1

    def canal_down(self):
        if self.__estado and self.__canal > 1:
            self.__canal -= 1

    def volumen_up(self):
        if self.__estado and self.__volumen < 7:
            self.__volumen += 1

    def volumen_down(self):
        if self.__estado and self.__volumen > 0:
            self.__volumen -= 1

    def get_control(self):
        return self.__control

    def set_control(self, control):
        self.__control = control

    @classmethod
    def get_num_tv(cls):
        return cls.numTV
