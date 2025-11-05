from persona import Persona
class Nuera(Persona):
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo ):
        super().__init__(nombre, apellido, apellido_nacimiento, sexo)
    
    def __str__(self):
        return f"La nuera se llama {self.nombre}, su apellido es {self.apellido}, su apellido de nacimiento es {self.apellido_nacimiento}, y su sexo es {self.sexo}"