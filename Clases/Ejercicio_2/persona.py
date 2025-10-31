class Persona:
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_nacimiento = apellido_nacimiento
        self.sexo = sexo
    def __str__(self):
        return f"{self.nombre, self.apellido, self.apellido_nacimiento, self.sexo}"