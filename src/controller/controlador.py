import sys
sys.path.append("src")
from Logica.calculadora import Usuario
import psycopg2
import SecretConfig

class ErrorNoEncontrado(Exception):
    pass

class ErrorNoInsertado(Exception):
    pass

class ErrorNoActualizado(Exception):
    pass

class ErrorNoBorrado(Exception):
    pass

def ObtenerCursor() :
    """
    Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones
    """
    DATABASE = SecretConfig.PGDATABASE
    USER = SecretConfig.PGUSER
    PASSWORD = SecretConfig.PGPASSWORD
    HOST = SecretConfig.PGHOST
    PORT = SecretConfig.PGPORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()

#Creacion de tabla
def CrearTabla():
    """
    Crea la tabla de usuarios, en caso de que no exista
    """    
    sql = ""
    with open("sql/crear-usuarios.sql","r") as f:
        sql = f.read()

    cursor = ObtenerCursor()

    try:
        cursor.execute( sql )
        cursor.connection.commit()
    except:
        # SI LLEGA AQUI, ES PORQUE LA TABLA YA EXISTE
        cursor.connection.rollback()

def BorrarFilas():
    """
    Borra todas las filas de la tabla (DELETE)
    ATENCION: EXTREMADAMENTE PELIGROSO.
    """
    sql = "Delete from usuarios;"
    cursor = ObtenerCursor()
    cursor.execute( sql )
    cursor.connection.commit()

#Insertar en la BD
def Insertar( usuario : Usuario ):
    """ Guarda un Usuario en la base de datos """
        # Todas las instrucciones se ejecutan a tavés de un cursor
    try:
        cursor = ObtenerCursor()
        if BuscarUsuariosExistentes(usuario.cedula) is False:
            raise ErrorNoInsertado(f"El usuario con cédula {usuario.cedula} ya existe.")
        else:
            cursor.execute(f"""
            insert into usuarios (
                cedula,   nombre,  basic_salary, start_work_date, last_vacation_date, accumulated_vacation_days
            )
            values 
            (
                '{usuario.cedula}',  '{usuario.nombre}', '{usuario.basic_salary}', '{usuario.start_date}', '{usuario.last_vacation_date}', '{usuario.accumulated_vacation_days}'
            );
                       """)
            cursor.connection.commit()
    except:
        raise ErrorNoInsertado(f"No se pudo insertar el usuario")   
#Modificar Datos

def Actualizar( usuario : Usuario ):
    """
    Actualiza los datos de un usuario en la base de datos

    El atributo cedula nunca se debe cambiar, porque es la clave primaria
    """
    try:
        cursor = ObtenerCursor()
        if BuscarUsuariosExistentes(usuario.cedula) == True:
            raise ErrorNoActualizado
        cursor.execute(f"""
            UPDATE usuarios
            SET
                nombre='{usuario.nombre}',
                basic_salary='{usuario.basic_salary}',
                start_work_date='{usuario.start_date}',
                last_vacation_date='{usuario.last_vacation_date}',
                accumulated_vacation_days='{usuario.accumulated_vacation_days}'
            where cedula='{usuario.cedula}'
            """)
        cursor.connection.commit()
    except:
        raise ErrorNoActualizado(f"No se pudo actualizar el registro con la cedula: {usuario.cedula}")

def Borrar( cedula:str ):
    """ Elimina la fila que contiene a un usuario en la BD """
    try:
        sql = f"delete from usuarios where cedula = '{cedula}'" 
        if BuscarUsuariosExistentes(cedula) == True:
            raise ErrorNoBorrado
        cursor = ObtenerCursor()
        cursor.execute( sql )
        cursor.connection.commit()
    except:
        raise ErrorNoBorrado(f"No se pudo borrar el registro con la cedula {cedula}")


#Consultar

def BuscarUsuarios( cedula: str ):
    """
    Carga de la DB las filas de la tabla usuarios
    """
    cursor = ObtenerCursor()
    cursor.execute(f""" Select nombre, cedula, basic_salary, start_work_date, last_vacation_date, 
        accumulated_vacation_days from usuarios where cedula = '{cedula}' """)
    
    lista = cursor.fetchone()

    if lista is None:
        raise ErrorNoEncontrado(f"No se encontro al usuario con la cedula = {cedula}")
    
    else:
        return Usuario(lista[1],lista[0],lista[2],lista[3], lista[4],lista[5])
    
def BuscarUsuariosExistentes( cedula: str ):
    """
    Carga de la DB las filas de la tabla usuarios
    """
    cursor = ObtenerCursor()
    cursor.execute(f""" Select nombre, cedula, basic_salary, start_work_date, last_vacation_date, 
        accumulated_vacation_days from usuarios where cedula = '{cedula}' """)
    
    lista = cursor.fetchone()

    if lista is None:
        return True
    
    else:
        return False
