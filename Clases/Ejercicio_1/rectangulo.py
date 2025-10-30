from figura import Figura

class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura
        
    def __str__(self):
        return f"Se ha creado un rectángulo de color { self.color}, base {self.base} y altura {self.altura}"
        
