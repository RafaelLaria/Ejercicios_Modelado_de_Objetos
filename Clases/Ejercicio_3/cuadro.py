class Cuadro:
    def __init__(self, titulo, AC, tecnica, subtecnica, soporte, autor, estado_conservacion):
        self.titulo = titulo
        self.AC = AC
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.autor = autor
        self.estado_conservacion = estado_conservacion
    def __str__(self):
        return f"{self.titulo, self.AC, self.tecnica, self.subtecnica, self.soporte, self.autor, self.estado_conservacion}"