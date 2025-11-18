class Actuacion:
    def __init__(self):
        self.fecha_inicio = ""
        self.fecha_fin = ""
        self.tipo = ""
    def __str__(self):
        return f'FECHA DE INICIO: {self.fecha_inicio}\n' \
               f'FECHA DE FINAL: {self.fecha_fin}\n' \
               f'TIPO: {self.tipo}'
    def dar_fecha1(self):
        self.fecha_inicio = input('Fecha de inicio:')
    def dar_fecha2(self):
        self.fecha_fin = input('Fecha de final:')
    def dar_tipo(self):
        print('Tipo de actuación:\n' \
              '1) Sondeo' \
              '2) Excavación' \
              '3) Seguimiento')
        self.tipo = input('Escoja un tipo de actuación:')
        if self.tipo == 1:
            print('Tipo: Sondeo')
        elif self.tipo == 2:
            print('Tipo: Excavación')
        elif self.tipo == 3:
            print('Tipo: Seguimiento')
        else:
            print('Escoja una de las tres opciones')
