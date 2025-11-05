from persona import Persona
class Hijo(Persona):
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo):
        super().__init__(nombre, apellido, apellido_nacimiento, sexo)
    def __str__(self):
        return f"El hijo se llama {self.nombre}, su apellido es {self.apellido} y su sexo es {self.sexo}"