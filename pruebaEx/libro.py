class Libro:
    nombre = str
    titulo = str
    ano = str

    def __init__(self, nombre, titulo, ano):
        self.nombre = nombre
        self.titulo = titulo
        self.ano = ano


class Fisico(Libro):
    material = str
    edicion = str
    numeroImpresion = str

    def __init__(self, nombre, titulo, ano, material, edicion, numeroImpresion):
        super().__init__(nombre, titulo, ano)
        self.material = material
        self.ano = ano
        self.edicion = edicion
        self.nombre = nombre
        self.titulo = titulo
        self.numeroImpresion = numeroImpresion

    def __str__(self):
        return f"los libros fisicos tienen {self.nombre} un {self.titulo}un{self.ano} y ademas como son impresos el {self.material}, tenemos tambien el {self.numeroImpresion}y ademas {self.edicion}"
