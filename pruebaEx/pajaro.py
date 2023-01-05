
#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO

class Pajaro:
    nombre=str
    especie=str
    color=str
    
    def __init__(self,nombre,especie,color):
        self.nombre=nombre
        self.especie=especie
        self.color=color
        
    def volar(self,metros):
        print(f"el pajaro a volado {metros} en metros")
        
pilloto=Pajaro("pepe","aguila","cafe",)

pilloto.volar(50)