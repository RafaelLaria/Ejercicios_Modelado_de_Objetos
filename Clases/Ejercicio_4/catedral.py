from edificio import Edificio
class Catedral(Edificio):
    def __init__(self, lugar, fecha_inicio, fecha_fin, fecha_BIC, material, estilo, nombre = "Catedral de Santiago de Compostela", culto = "Católico", fecha_1consagracion = "1128", fecha_2inicio = "1168", fecha_2consagracion = "1211"):
        super().__init__(lugar, fecha_inicio, fecha_fin, fecha_BIC, material, estilo)
        self.nombre = nombre
        self.culto = culto
        self.fecha_1consagracion = fecha_1consagracion
        self.fecha_2inicio = fecha_2inicio
        self.fecha_2consagracion= fecha_2consagracion
    def __str__(self):
        f"La {self.nombre} es un templo de culto {self.culto} situado en {self.lugar}.\nLa construcción se inició en {self.fecha_inicio} y se construyó fundamentalmente en {self.material}. Se terminó en {self.fecha_fin} y se consagró por primera vez en {self.fecha_1consagracion}.\nLa construcción se continuó en {self.fecha_2inicio} y se consgró definitivamente en {self.fecha_2consagracion}.\nFue declarada Bien de Interés Cultural en {self.fecha_BIC} y emplea múltiples estilos arquitectónicos: {self.estilo}"