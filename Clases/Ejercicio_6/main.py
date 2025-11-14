from persona import Persona

persona = Persona(nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo, numero_identificacion)
nombre = persona.dar_nombre()
primer_apellido, segundo_apellido = persona.dar_apellidos()
fecha_nacimiento = persona.dar_fecha()
sexo = persona.dar_sexo()
numero_identificacion = persona.dar_numero()

print(persona)
