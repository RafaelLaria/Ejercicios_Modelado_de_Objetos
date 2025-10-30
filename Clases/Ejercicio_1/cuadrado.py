from figura import Figura

class Cuadrado(Figura):
    def __init__(self, color,  lado):
        super().__init__(color)
        self.lado = lado
        
    def __str__(self):
        return f"Se ha creado un cuadrado de color {self.color} y lado {self.lado}"

