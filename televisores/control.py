class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        self.tv = tv

    def set_tv(self, tv):
        self.tv = tv

    def get_tv(self):
        return self.tv

    # Métodos para controlar el televisor
    def turn_on(self):
        if self.tv:
            self.tv.estado = True

    def turn_off(self):
        if self.tv:
            self.tv.estado = False

    def set_canal(self, canal):
        if self.tv:
            self.tv.set_canal(canal)

    def canal_up(self):
        if self.tv:
            self.tv.canal_up()

    def canal_down(self):
        if self.tv:
            self.tv.canal_down()

    def set_volumen(self, volumen):
        if self.tv:
            self.tv.set_volumen(volumen)

    def volumen_up(self):
        if self.tv:
            self.tv.volumen_up()

    def volumen_down(self):
        if self.tv:
            self.tv.volumen_down()
