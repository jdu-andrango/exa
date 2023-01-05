from accion import Accion
from libro import Libro
from comedia import Comedia


class libreria:
    nombreLibreria= str
    lugar=str
    libro= Libro("","","","","","")
    accion= Accion("","")
    comedia= Comedia("","")
    
    def __init__(self,nombreLibreria,lugar,libro,accion,comedia) -> None:
        self.nombreLibreria=nombreLibreria
        self.lugar=lugar
        