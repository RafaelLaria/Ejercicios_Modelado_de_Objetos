from figura import Figura

class Elipse(Figura):
    def __init__(self, color, eje_mayor, eje_menor):
        super().__init__(color)
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        
    def __str__(self):
        return f"Se ha creado una elipse de color {self.color}, eje mayor {self.eje_mayor} y eje menor {self.eje_menor}"
    
    
        
