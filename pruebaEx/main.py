from libro import Libro
from libro import Fisico
from accion import Accion
from comedia import Comedia
from cienciaFiccion import libreria

if __name__ == "__main__":
    libro1 = Fisico("1", "1", "1", "1", "1", "1")
    gerra = Accion("a", "a")
    risas = Comedia("1", "1", "1", "1")
    librosBonitos= libreria("sads","asdhkj",libro1,gerra,risas)




print(libro1)

print(risas.comparacion(gerra))

print(libreria)


