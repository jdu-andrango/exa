##CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__

class Libro:
    titulo:str
    editorial:str
    autor:str
    
    def __init__(self,titulo, editorial, autor):
        self.titulo=titulo
        self.editorial=editorial
        self.autor=autor
    
    def __str__(self):
        return f"todos nuestro libros poseen {self.titulo}, la editorial {self.editorial}, y el nombre de su autor: {self.autor}"

librito= Libro("las aventuras de python","yavirax","jonathan",)
print(librito)
        
    