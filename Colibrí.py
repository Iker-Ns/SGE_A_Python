class Colibrí:
    def __init__(self, edad, color_del_pelaje, velocidad_maxima, peso, genero) -> None:
        self._edad = edad
        self._color_del_pelaje = color_del_pelaje
        self._velocidad_maxima = velocidad_maxima
        self._peso = peso
        self._genero = genero

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_color_del_pelaje(self):
        return self._color_del_pelaje

    def set_color_del_pelaje(self, color_del_pelaje):
        self._color_del_pelaje = color_del_pelaje

    def get_velocidad_maxima(self):
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self._velocidad_maxima = velocidad_maxima

    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso

    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero
