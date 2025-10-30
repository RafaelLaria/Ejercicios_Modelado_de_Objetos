from figura import Figura

class Circulo(Figura):
    def __init__(self, color, diametro):
        super().__init__(color)
        self.diametro = diametro
        
    def __str__(self):
        return f"Se ha creado un círculo de color {self.color} y diámetro {self.diametro}"