from persona import Persona
class Carlos(Persona):
    def __init__(self, nombre, apellido, sexo):
        super().__init__(nombre, apellido, sexo)
    def __str__(self):
        return f"La persona tiene nombre {self.nombre}, apellido {self.apellido} y sexo {self.sexo}"