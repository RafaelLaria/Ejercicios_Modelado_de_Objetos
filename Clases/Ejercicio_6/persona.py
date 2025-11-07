class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo, numero_identificacion):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion
    def __str__(self):
        return (f"Nombre y apellidos: {self.nombre} {self.primer_apellido} {self.segundo_apellido}\n"
                f"Fecha de nacimiento : {self.fecha_nacimiento}\n"
                f"Número de identificación: {self.numero_identificacion}")
    def dar_nombre():
        nombre = str(input("Escriba el nombre"))
        return print(nombre)
    def dar_apellidos():
        primer_apellido = str(input("Escriba el primer apellido"))
        segundo_apellido = str(input("Escriba el segundo apellido"))
        return primer_apellido, segundo_apellido
    def dar_fecha():
        fecha_nacimiento = str(input("Escriba la fecha de nacimiento"))
        return fecha_nacimiento
    def dar_sexo():
        sexo = str(input("Escriba el sexo"))
        return sexo
    def dar_numero():
        numero_identificacion = str(input("Escriba el número de identificación"))
        if len(numero_identificacion) == 9 and numero_identificacion[8] == int:
            print(numero_identificacion)
        else:
            print("ERROR: El número de identificación debe tener exactamente 9 caracteres y la ultima debe ser un número")
        return True
    