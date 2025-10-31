from persona import Persona
class Kate(Persona):
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo ):
        super().__init__(nombre, apellido, apellido_nacimiento, sexo)
    
    def __str__(self):
        return f"La persona tiene nombre {self.nombre}, apellido {self.apellido}, apellido de nacimiento {self.apellido_nacimiento}, y de sexo {self.sexo}"