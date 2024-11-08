import sys
sys.path.append("src")
import psycopg2
from contextlib import closing
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
    """Crea la tabla de usuarios si no existe."""
    with open("sql/crear-usuarios.sql", "r") as f:
        sql = f.read()
    
    with closing(ObtenerConexion()) as conn, conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            conn.commit()
        except psycopg2.errors.DuplicateTable:
            conn.rollback()

def BorrarFilas():
    """Borra todas las filas de la tabla usuarios."""
    sql = "DELETE FROM usuarios;"
    with closing(ObtenerConexion()) as conn, conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()

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
        conexion.commit()  # Usa la conexión para hacer commit
    except:
        raise ErrorNoInsertado(f"No se pudo insertar el usuario: {usuario.cedula}")


# Modificar Datos
def Actualizar(usuario: Usuario):
    """
    Actualiza los datos de un usuario en la base de datos.
    """
    conexion = ObtenerConexion()
    try:
        if not BuscarUsuariosExistentes(usuario.cedula):
            raise ErrorNoActualizado(f"No se encontró el usuario con cédula: {usuario.cedula}")

        conexion.execute(f"""
            UPDATE usuarios
            SET
                nombre = %s,
                basic_salary = %s,
                start_work_date = %s,
                last_vacation_date = %s,
                accumulated_vacation_days = %s
            WHERE cedula = %s
        """, (usuario.nombre, usuario.basic_salary, usuario.start_date, usuario.last_vacation_date, usuario.accumulated_vacation_days, usuario.cedula))

        conexion.commit()
        print(f"Usuario con cédula {usuario.cedula} actualizado exitosamente.")
    except Exception as e:
        conexion.rollback()
        raise ErrorNoActualizado(f"No se pudo actualizar el registro con la cédula: {usuario.cedula}. Error: {str(e)}")
    finally:
        conexion.close()


# Borrar Usuario
def Borrar(cedula: str):
    """Elimina un usuario de la base de datos según su cédula."""
    sql = "DELETE FROM usuarios WHERE cedula = %s"
    if not BuscarUsuariosExistentes(cedula):
        raise ErrorNoBorrado(f"No se encontró el usuario con cédula: {cedula}")
    
    with closing(ObtenerConexion()) as conn, conn.cursor() as cursor:
        try:
            cursor.execute(sql, (cedula,))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise ErrorNoBorrado(f"No se pudo borrar el usuario: {str(e)}")

# Consultar Usuario
def BuscarUsuarios(cedula: str) -> Usuario:
    """Busca y devuelve un usuario según la cédula."""
    sql = """
        SELECT nombre, cedula, basic_salary, start_work_date, last_vacation_date, accumulated_vacation_days
        FROM usuarios WHERE cedula = %s
    """
    with closing(ObtenerConexion()) as conn, conn.cursor() as cursor:
        cursor.execute(sql, (cedula,))
        resultado = cursor.fetchone()
        if resultado is None:
            raise ErrorNoEncontrado(f"No se encontró el usuario con cédula: {cedula}")
        
        return Usuario(*resultado)

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
