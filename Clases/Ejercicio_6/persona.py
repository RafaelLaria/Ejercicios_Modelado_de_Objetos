class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, numero_identificacion):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.numero_identificacion = numero_identificacion
    def __str__(self):
        return (f"Nombre y apellidos: {self.nombre} {self.primer_apellido} {self.segundo_apellido}\n"
                f"Fecha de nacimiento : {self.fecha_nacimiento}\n"
                f"Número de identificación: {self.numero_identificacion}")