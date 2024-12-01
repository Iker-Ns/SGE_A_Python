class Coche:
    def __init__(self, marca, modelo, año_fabricacion, color, velocidad_maxima):
        self._marca = marca
        self._modelo = modelo
        self._año_fabricacion = año_fabricacion
        self._color = color
        self._velocidad_maxima = velocidad_maxima

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_año_fabricacion(self):
        return self._año_fabricacion

    def set_año_fabricacion(self, año_fabricacion):
        self._año_fabricacion = año_fabricacion

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_velocidad_maxima(self):
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self._velocidad_maxima = velocidad_maxima
