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

def ObtenerConexion():
    """Establece una conexión con la base de datos."""
    return psycopg2.connect(
        database=SecretConfig.PGDATABASE,
        user=SecretConfig.PGUSER,
        password=SecretConfig.PGPASSWORD,
        host=SecretConfig.PGHOST,
        port=SecretConfig.PGPORT
    )

def ObtenerCursor():
    """
    Retorna un cursor para ejecutar instrucciones, manteniendo la misma conexión abierta.
    """
    conexion = ObtenerConexion()
    return conexion.cursor()

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
    sql = """
        INSERT INTO usuarios (cedula, nombre, basic_salary, start_work_date, last_vacation_date, accumulated_vacation_days)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    if not BuscarUsuariosExistentes(usuario.cedula):
        raise ErrorNoInsertado(f"El usuario con cédula {usuario.cedula} ya existe.")
    
    conexion = ObtenerConexion()  # Obtén la conexión por separado
    cursor = ObtenerCursor()  # Obtén solo el cursor
    
    try:
        cursor.execute(sql, (usuario.cedula, usuario.nombre, usuario.salario_basico, usuario.fecha_inicio, usuario.fecha_ultimo_vacaciones, usuario.dias_vacaciones_acumulados))
        conexion.commit()  # Usa la conexión para hacer commit
    except Exception as e:
        conexion.rollback()  # Asegúrate de hacer rollback si ocurre un error
        raise ErrorNoInsertado(f"No se pudo insertar el usuario: {str(e)}")
    finally:
        cursor.close()  # Cierra el cursor después de la operación
        conexion.close()  # Cierra la conexión después de la operación


# Modificar Datos
def Actualizar(usuario: Usuario):
    """
    Actualiza los datos de un usuario en la base de datos.
    El atributo cedula nunca se debe cambiar, porque es la clave primaria.
    """
    try:
        conexion, cursor = ObtenerCursor()  # Desempaqueta la tupla correctamente
        # Verifica si el usuario existe antes de intentar actualizar
        if not BuscarUsuariosExistentes(usuario.cedula):
            raise ErrorNoActualizado(f"No se encontró el usuario con la cédula: {usuario.cedula}")
        
        cursor.execute(f"""
            UPDATE usuarios
            SET
                nombre='{usuario.nombre}',
                basic_salary='{usuario.salario_basico}',
                start_work_date='{usuario.fecha_inicio}',
                last_vacation_date='{usuario.fecha_ultimo_vacaciones}',
                accumulated_vacation_days='{usuario.dias_vacaciones_acumulados}'
            WHERE cedula='{usuario.cedula}'
        """)
        conexion.commit()  # Usar la conexión para hacer commit
    except Exception as e:
        raise ErrorNoActualizado(f"No se pudo actualizar el registro con la cédula: {usuario.cedula}. Error: {str(e)}")


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
    cursor = ObtenerCursor()
    cursor.execute(f"SELECT 1 FROM usuarios WHERE cedula = '{cedula}'")
    resultado = cursor.fetchone()
    return resultado is not None  # Retorna True si el usuario existe

