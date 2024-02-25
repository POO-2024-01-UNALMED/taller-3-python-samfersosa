class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)

    def setTv(self, tv):
        self.tv = tv

    def getTv(self):
        return self.tv

    def turnOn(self):
        if self.tv:
            self.tv.turnOn()

    def turnOff(self):
        if self.tv:
            self.tv.turnOff()

    def canalUp(self):
        if self.tv:
            self.tv.setCanal(self.tv.getCanal() + 1)

    def canalDown(self):
        if self.tv:
            self.tv.setCanal(self.tv.getCanal() - 1)

    def volumenUp(self):
        if self.tv:
            self.tv.setVolumen(self.tv.getVolumen() + 1)

    def volumenDown(self):
        if self.tv:
            self.tv.setVolumen(self.tv.getVolumen() - 1)

    def setCanal(self, canal):
        if self.tv:
            self.tv.setCanal(canal)

    def setVolumen(self, volumen):
        if self.tv:
            self.tv.setVolumen(volumen)
