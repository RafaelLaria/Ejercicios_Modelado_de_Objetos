from cuadro import Cuadro
class Original(Cuadro):
    def __init__(self, titulo, AC, tecnica, subtecnica, soporte, autor, estado_conservacion, institucion, ciudad, pais):
        super().__init__(titulo, AC, tecnica, subtecnica, soporte, autor, estado_conservacion)
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais
    def __str__(self):
        return f"El título del cuadro original es {self.titulo}, se pintó entre {self.AC}, \nla técnica usada fue {self.tecnica} y la subtecnica {self.subtecnica}.\nEl marco usado es de {self.soporte}.\n Su autor es {self.autor}, actualmente se encuentra en {self.institucion}, {self.ciudad}, {self.pais}"