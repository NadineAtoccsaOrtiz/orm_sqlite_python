import  orm 
from tablas.productos import Productos
from tablas.clientes import Clientes
db=orm.SQLiteORM('Tienda')

db.crear_tabla(Productos)
db.crear_tabla(Clientes)

# data={
#     'nombre':'detergente patito',
#     'precio':2.5,
#     'descripcion':'limpia',
#     'cantidad':10
# }

# db.insertarUno('productos',data)

# print(db.mostrar('productos'))

# data=[
#     {
#         'nombre':'china',
#         'DNI':78546956,
#         'celular':987456321,
#         'f_nacimiento':'13/02/12'
#     },
#     {
#         'nombre':'mochi',
#         'DNI':78554873,
#         'celular':987121561,
#         'f_nacimiento':'10/02/04'
#     }
# ]
# db.insertarVarios('Clientes',data)

# data={'f_nacimiento':'10/10/2003'}
# db.actualizar('Clientes', data,'id=2')
# db.eliminar('Clientes','dni=78546956')

# print(db.mostrar('Clientes',type='objeto'))
# print(db.mostrar('Clientes'))
# print(db.mostrar('Clientes',where='dni=78554873',type='objeto'))
print(db.mostrar('Clientes',where="nombre LIKE '%c%'",type='objeto')) # like para buscar sin saber el nom,bre completo, al final , al inicio o intermedio
db.cerrar()

# tarea usando la orm lo vamos a integrar a la base de datos en 'mi apk'
