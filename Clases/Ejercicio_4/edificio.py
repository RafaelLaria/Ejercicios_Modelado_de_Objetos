class Edificio:
    def __init__(self, lugar, fecha_inicio, fecha_fin, fecha_BIC, material, estilo):
        self.lugar = lugar
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_BIC = fecha_BIC
        self.material = material
        self.estilo = estilo
    def __str__(self):
        return f"{self.lugar, self.fecha_inicio, self.fecha_fin, self.fecha_BIC, self.material, self.estilo}"
    