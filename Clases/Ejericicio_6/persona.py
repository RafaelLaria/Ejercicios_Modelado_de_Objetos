class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo, numero_identificacion):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion
    def __str__(self):
        return f'NOMBRE: {self.nombre}\n' \
               f'APELLIDO 1: {self.primer_apellido}\n' \
               f'APELLIDO 2: {self.segundo_apellido}\n' \
               f'FECHA DE NACIMIENTO: {self.fecha_nacimiento}\n' \
               f'SEXO:{self.sexo}\n' \
               f'NUMERO DE IDENTIFICACION: {self.numero_identificacion}\n'
    
    def dar_nombre(self):
        self.nombre = input('Nombre:')
    def dar_apellido1(self):
        self.primer_apellido = input('Apellido1:')
    def dar_apellifo2(self):
        self.segundo_apellido = input('Apellido2:')
    def dar_fecha(self):
        self.fecha_nacimiento = int(input('Fecha de nacimiento:'))
    def dar_sexo(self):
        self.sexo = input('Dar sexo:')
    def dar_numero(self):
        self.numero_identificacion = input('Número de identificación:')
        if len(self.numero_identificacion) == 9 and self.numero_identificacion[9] == str and self.numero_identificacion[0:8] == int:
            print(self.numero_identificacion)
        else:
            print('El numero de identificación debe tener 8 caracteres, el ultimo siendo una letra')