from accion import Accion


class Comedia(Accion):
    edadMaxima = str
    edadMinima = str

    def __init__(self, sangre, sinSangre, edadMaxima, edadMinima):
        super().__init__(sangre, sinSangre)
        self.edadMaxima = edadMaxima
        self.edadMinima = edadMinima

    def comparacion(self, otro_genero):
        return f"los libros de comedia tienen {self.edadMaxima} y una {self.edadMinima} en comparacion a los libros {otro_genero.sangre} y sin {otro_genero.sinSangre}"

