class TV:
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1  # Atributo para almacenar el canal actual
        self.volumen = 1  # Atributo para almacenar el volumen actual
        self.control = None  # Atributo para almacenar el control remoto asociado

    # Métodos getter y setter para los atributos de la clase TV
    def get_canal(self):
        return self.canal

    def set_canal(self, canal):
        self.canal = canal

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, volumen):
        self.volumen = volumen

    def get_estado(self):
        return self.estado

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def set_control(self, control):
        self.control = control

    def get_control(self):
        return self.control

    # Métodos para cambiar el canal hacia arriba y hacia abajo
    def canal_up(self):
        self.canal += 1

    def canal_down(self):
        self.canal -= 1

    # Métodos para cambiar el volumen hacia arriba y hacia abajo
    def volumen_up(self):
        self.volumen += 1

    def volumen_down(self):
        self.volumen -= 1
