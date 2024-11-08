import sys
sys.path.append("src")
import psycopg2
import SecretConfig
from Logica.calculadora import Usuario

# Definición de excepciones personalizadas
class ErrorNoEncontrado(Exception):
    pass

class ErrorNoInsertado(Exception):
    pass

class ErrorNoActualizado(Exception):
    pass

class ErrorNoBorrado(Exception):
    pass

class ErrorConexionBD(Exception):
    pass 

class ErrorNoSeCreoLaBD(Exception):
    pass

def ObtenerConexion():
    """
    Crea la conexión a la base de datos.
    """
    try:
        DATABASE = SecretConfig.PGDATABASE
        USER = SecretConfig.PGUSER
        PASSWORD = SecretConfig.PGPASSWORD
        HOST = SecretConfig.PGHOST
        PORT = SecretConfig.PGPORT
        conexion = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        return conexion.cursor()
    except:
        raise ErrorConexionBD(f"No fue posible hacer la conexion con la BD")

# Creación de tabla
def CrearTabla():
    """
    Crea la tabla de usuarios, en caso de que no exista
    """    
    sql = ""
    with open("sql/crear-usuarios.sql","r") as f:
        sql = f.read()

    cursor = ObtenerConexion()

    try:
        cursor.execute( sql )
        cursor.connection.commit()
    except:
        cursor.connection.rollback()

def BorrarFilas():
    """Borra todas las filas de la tabla usuarios."""
    sql = "DELETE FROM usuarios;"
    cursor = ObtenerConexion()
    cursor.execute(sql)
    cursor.connection.commit()

# Insertar en la BD
def Insertar(usuario: Usuario):
    """Guarda un Usuario en la base de datos."""
    sql = f"""
        INSERT INTO usuarios (cedula, nombre, basic_salary, start_work_date, last_vacation_date, accumulated_vacation_days)
        VALUES ('{usuario.cedula}','{usuario.nombre}','{usuario.salario_basico}','{usuario.fecha_inicio}','{usuario.fecha_ultimo_vacaciones}','{usuario.dias_vacaciones_acumulados}');
    """
    if BuscarUsuariosExistentes(usuario.cedula) == True:
        raise ErrorNoInsertado(f"El usuario con cédula {usuario.cedula} ya existe.")
    
    conexion = ObtenerConexion()  # Obtén la conexión por separado
    
    try:
        conexion.execute(sql)
        conexion.connection.commit()  # Usa la conexión para hacer commit
    except:
        raise ErrorNoInsertado(f"No se pudo insertar el usuario: {usuario.cedula}")


# Modificar Datos
def Actualizar(cedula: str, nombre, salario_basico, fecha_inicio, fecha_ultimo_vacaciones, dias_vacaciones_acumulados):
    """
    Actualiza los datos de un usuario en la base de datos.
    """
    conexion = ObtenerConexion()
    try:
        if BuscarUsuariosExistentes(cedula) == False:
            raise ErrorNoActualizado(f"No se encontró el usuario con cédula: {cedula}")

        conexion.execute(f"""
            UPDATE usuarios
            SET
                nombre = '{nombre}',
                basic_salary = '{salario_basico}',
                start_work_date = '{fecha_inicio}',
                last_vacation_date = '{fecha_ultimo_vacaciones}',
                accumulated_vacation_days = '{dias_vacaciones_acumulados}'
            WHERE cedula = '{cedula}';
        """)
        conexion.connection.commit()
        return f"Usuario con cédula {cedula}, fue actualizado exitosamente."
    except:
        raise ErrorNoActualizado(f"No se pudo actualizar el registro con la cédula: {cedula}")


# Borrar Usuario
def Borrar(cedula: str):
    """Elimina un usuario de la base de datos según su cédula."""
    sql = f"""DELETE FROM usuarios WHERE cedula = '{cedula}'"""
    if BuscarUsuariosExistentes(cedula) == False:
        raise ErrorNoBorrado(f"No se encontró el usuario con cédula: {cedula}")
    cursor = ObtenerConexion()
    try:
        cursor.execute(sql)
        cursor.connection.commit()
        return f"usuario borrado Exitosamente"
        
    except:
        raise ErrorNoBorrado(f"No se pudo borrar el usuario: {cedula}")

# Consultar Usuario
def BuscarUsuarios(cedula: str) -> Usuario:
    """Busca y devuelve un usuario según la cédula."""
    sql = f"""
        SELECT nombre, cedula, basic_salary, start_work_date, last_vacation_date, accumulated_vacation_days FROM usuarios WHERE cedula = '{cedula}' 
    """
    cursor = ObtenerConexion()
    cursor.execute(sql)
    resultado = cursor.fetchone()
    if resultado is None:
        raise ErrorNoEncontrado(f"No se encontró el usuario con cédula: {cedula}")
        
    return Usuario(resultado[1], resultado[0], resultado[2], resultado[3], resultado[4], resultado[5])

# Verificar si un Usuario existe
def BuscarUsuariosExistentes(cedula: str) -> bool:
    """
    Verifica si un usuario con la cédula dada existe en la base de datos.
    Retorna True si existe, False en caso contrario.
    """
    cursor = ObtenerConexion()
    cursor.execute(f"SELECT FROM usuarios WHERE cedula = '{cedula}'")
    resultado = cursor.fetchone()
    if resultado is None:
        return False
    else:
        return True
