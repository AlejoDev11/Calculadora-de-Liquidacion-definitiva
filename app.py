import sys
sys.path.append("src")

from flask import Flask, render_template, request, flash
from controller.controlador import Insertar, Actualizar, Borrar, BuscarUsuarios, ErrorNoInsertado, ErrorNoActualizado, ErrorNoBorrado, ErrorNoEncontrado
from Logica.calculadora import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    """Página de inicio."""
    return render_template('index.html')

@app.route('/insertar')
def insertar():
    """Ruta para insertar un nuevo usuario."""
    return render_template('insertar.html')

@app.route('/insertado')
def insertado():
    """Ruta para insertar un nuevo usuario."""
    cedula = request.args["cedula"]
    nombre = request.args["nombre"]
    basic_salary = request.args["basic_salary"]
    start_date = request.args["start_date"]
    last_vacation_date = request.args["last_vacation_date"]
    accumulated_vacation_days = request.args["accumulated_vacation_days"]
    motivo_finalizacion = request.args["motivo_finalizacion"]
        
    usuario = Usuario(cedula, nombre, basic_salary, start_date, last_vacation_date, accumulated_vacation_days, motivo_finalizacion)
        
    try:
        Insertar(usuario)
        return f"El usuario fue insertado exitosamente"
    except:
        raise ErrorNoInsertado(f"El usuario no pudo ser insertado")


@app.route('/actualizar')
def actualizar():
    """Ruta para actualizar un usuario existente."""
    return render_template('actualizar.html')

@app.route('/actualizado')
def actualizado():
    """Ruta para actualizar un usuario existente."""
    cedula = request.args['cedula']
    nombre = request.args['nombre']
    basic_salary = request.args['basic_salary']
    start_date = request.args['start_date']
    last_vacation_date = request.args['last_vacation_date']
    accumulated_vacation_days = request.args['accumulated_vacation_days']
    motivo_finalizacion = request.args["motivo_finalizacion"]
        
    usuario = Usuario(cedula, nombre, basic_salary, start_date, last_vacation_date, accumulated_vacation_days, motivo_finalizacion)
        
    try:
        Actualizar(usuario.cedula, usuario.nombre, usuario.salario_basico, usuario.fecha_inicio, usuario.fecha_ultimo_vacaciones, usuario.dias_vacaciones_acumulados, usuario.motivo_finalizacion)
        return f"El usuario ha sido actualizado "
    except:
        raise ErrorNoActualizado(f"No se pudo actualizar el usuario con la cedula {cedula}")

@app.route('/borrar')
def borrar():
    """Ruta para borrar un usuario según su cédula."""
    return render_template('borrar.html')
    
@app.route('/borrado')
def borrado():
    """Ruta para borrar un usuario según su cédula."""

    cedula = request.args['cedula']    
    try:
        Borrar(cedula)
        return f"El usuario ha sido borrado exitosamente"        
    except:
        raise ErrorNoBorrado(f"No se pudo borrar el usuario {cedula}")

@app.route('/buscar')
def buscar():
    """Ruta para buscar un usuario según su cédula."""
    return render_template('buscar.html')

@app.route('/buscado')
def buscado():
    """Ruta para buscar un usuario según su cédula."""
    usuario = None
    cedula = request.args['cedula']
        
    try:
        usuario = BuscarUsuarios(cedula)
        return render_template('buscar.html', usuario=usuario)
            
    except:
        raise ErrorNoEncontrado(f"No se pudo encontrar al usuario {cedula}")

if __name__ == '__main__':
    app.run(debug=True)
