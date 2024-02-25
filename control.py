class Control:
    def __init__(self):
        self.__tv = None

    def turn_on(self):
        if self.__tv:
            self.__tv.turn_on()

    def turn_off(self):
        if self.__tv:
            self.__tv.turn_off()

    def canal_up(self):
        if self.__tv:
            self.__tv.canal_up()

    def canal_down(self):
        if self.__tv:
            self.__tv.canal_down()

    def volumen_up(self):
        if self.__tv:
            self.__tv.volumen_up()

    def volumen_down(self):
        if self.__tv:
            self.__tv.volumen_down()

    def set_canal(self, canal):
        if self.__tv:
            self.__tv.set_canal(canal)

    def set_volumen(self, volumen):
        if self.__tv:
            self.__tv.set_volumen(volumen)

    def enlazar(self, tv):
        self.__tv = tv

    def get_tv(self):
        return self.__tv
