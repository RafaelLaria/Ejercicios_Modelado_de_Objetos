class Miembro:
    def __init__(self):
        self.nombre1 = ""
        self.apellidos = ""
        self.rol = ""
    def __str__(self):
        return 'MIEMBRO\n' \
        f'NOMBRE DE MIEMBRO: {self.nombre1}\n' \
        f'APELLIDOS: {self.apellidos}\n' \
        f'ROL: {self.rol}'
    def dar_miembro(self):
        self.nombre1 = input('Nombre del miembro:')
    def dar_apellidos(self):
        self.apellidos = input('Apellidos:')
    def dar_rol(self):
        self.rol = input('Rol:')