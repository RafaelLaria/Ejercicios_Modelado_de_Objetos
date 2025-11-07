class Lugar:
    def __init__(self, nombre1, coordenada_x, coordenada_y):
        self.nombre1 = nombre1
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
    def __str__(self):
        return f"{self.nombre1, self.coordenada_x, self.coordenada_y}"