class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, numero_identificacion):
        self.nombre = str(input("Escriba el nombre"))
        self.primer_apellido = str(input("Escriba el primer apellido"))
        self.segundo_apellido = str(input("Escriba el segundo apellido"))
        self.fecha_nacimiento = str(input("Escriba la fecha de nacimiento"))

        while True:
            num = str(input("Escriba el número de identificación"))
            if len(num) == 9:
                self.numero_identificacion = num
            else:
                print("El número de identificación debe tener 9 caracteres")
                break
    def __str__(self):
        return (f"Nombre y apellidos: {self.nombre} {self.primer_apellido} {self.segundo_apellido}\n"
                f"Fecha de nacimiento : {self.fecha_nacimiento}\n"
                f"Número de identificación: {self.numero_identificacion}")