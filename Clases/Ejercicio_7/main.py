from proyecto import Proyecto
from miembro import Miembro
from lugar import Lugar
 
p = Proyecto()
p.dar_nombre()
p.dar_fecha1()
p.dar_fecha2()

m = Miembro()
m.dar_miembro()
m.dar_apellidos()
m.dar_rol()

l = Lugar()
l.dar_nombre2()
l.dar_x()
l.dar_y()

print(p)
print(m)
print(l)