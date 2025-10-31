from persona import Persona
class Diana(Persona):
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo):
        super().__init__(nombre, apellido, apellido_nacimiento, sexo)
    def __str__(self):
        return f"La person tiene nombre {self.nombre}, apellido {self.apellido}, apellido de nacimiento {self.apellido_nacimiento} y sexo {self.sexo}"