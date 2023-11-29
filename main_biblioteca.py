import orm
from tabla_biblioteca.autores import Autores
from tabla_biblioteca.libros import Libros
from tabla_biblioteca.usuarios import Usuarios

db=orm.SQLiteORM('db_Biblioteca')

# db.crear_tabla(Autores)
# db.crear_tabla(Libros)
# db.crear_tabla(Usuarios)

# {'clave':'valor'} objeto

nuevo_autor={
    'dni':72578574,
    'nombre':'Quevedo',
    'apellidos':'escoja de los rios'}

nuevos_usuarios=[
    {
        'DNI':74757878,
        'nombre':'Maria',
        'apellidos':'Limascca',
        'f_nacimiento':'12/05/2004',
        'estado':'activo'
    },
    {
        'DNI':74526984,
        'nombre':'feli',
        'apellidos':'ccaccachahua',
        'f_nacimiento':'12/05/2004',
        'estado':'activo'
    },
    {
        'DNI':74658475,
        'nombre':'bichota',
        'apellidos':'de taype',
        'f_nacimiento':'28/11/2023',
        'estado':'inactivo'
    },
    {
        'DNI':74265841,
        'nombre':'chamo',
        'apellidos':'no jodas',
        'f_nacimiento':'30/11/2023',
        'estado':'activo'
    },
    {
        'DNI':74978945,
        'nombre':'yadira',
        'apellidos':'quiero mani',
        'f_nacimiento':'509 a.c',
        'estado':'momia'
    }
]

# db.insertarUno('Autores',nuevo_autor)
# db.insertarVarios('Usuarios',nuevos_usuarios)

## muestra una lista e tuuplas 
# print(db.mostrar('Usuarios'))
## muestra un objeto con sus campos y sus valores
# print(db.mostrar('Usuarios',type='objeto'))
## muestra infornmacion filtrada
# print(db.mostrar('Usuarios',where="estado='momia'",type='objeto'))
# print(db.mostrar('Usuarios',where="nombre LIKE 'cha%'",type='objeto')) #HACIENDO USO DE %, solon funciona  en texto, no con numero
# print(db.mostrar('Usuarios',where="dni=74265841",type='objeto')) 

# db.actualizar('Usuarios',{'estado':'activo'},where="nombre='yadira'")
# db.actualizar('Usuarios',{'f_nacimiento':'11/08/2005'},where='dni=74978945')
# dato_actualizar={'nombre':'chamo','apellidos':'ya es salida'}
# db.actualizar('Usuarios',dato_actualizar,where='dni=74265841')
# print(db.mostrar('Usuarios',type='objeto'))

db.eliminar('Usuarios',where="dni=74265841")