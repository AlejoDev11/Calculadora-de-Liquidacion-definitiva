import sys
sys.path.append("src")

from flask import Flask, render_template, request, redirect, url_for, flash
from controller.controlador import Insertar, Actualizar, Borrar, BuscarUsuarios, ErrorNoInsertado
from Logica.calculadora import Usuario

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave segura

@app.route('/')
def index():
    """Página de inicio."""
    return render_template('index.html')

@app.route('/insertar', methods=['GET', 'POST'])
def insertar_usuario():
    """Ruta para insertar un nuevo usuario."""
    cedula = request.args["cedula"]
    nombre = request.args["nombre"]
    basic_salary = request.args["basic_salary"]
    start_date = request.args["start_date"]
    last_vacation_date = request.args["last_vacation_date"]
    accumulated_vacation_days = request.args["accumulated_vacation_days"]
        
    usuario = Usuario(cedula, nombre, basic_salary, start_date, last_vacation_date, accumulated_vacation_days)
        
    try:
        Insertar(usuario)
    except:
        raise ErrorNoInsertado(f"El usuario no pudo ser insertado")
    
    return f"El usuario fue insertado exitosamente"

@app.route('/actualizar', methods=['GET', 'POST'])
def actualizar_usuario():
    """Ruta para actualizar un usuario existente."""
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        basic_salary = request.form['basic_salary']
        start_date = request.form['start_date']
        last_vacation_date = request.form['last_vacation_date']
        accumulated_vacation_days = request.form['accumulated_vacation_days']
        
        usuario = Usuario(cedula, nombre, basic_salary, start_date, last_vacation_date, accumulated_vacation_days)
        
        try:
            Actualizar(usuario)
            flash('Usuario actualizado exitosamente.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al actualizar usuario: {str(e)}', 'danger')
    
    return render_template('actualizar.html')

@app.route('/borrar', methods=['GET', 'POST'])
def borrar_usuario():
    """Ruta para borrar un usuario según su cédula."""
    if request.method == 'POST':
        cedula = request.form['cedula']
        
        try:
            Borrar(cedula)
            flash('Usuario borrado exitosamente.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al borrar usuario: {str(e)}', 'danger')
    
    return render_template('borrar.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_usuario():
    """Ruta para buscar un usuario según su cédula."""
    usuario = None
    if request.method == 'POST':
        cedula = request.form['cedula']
        
        try:
            usuario = BuscarUsuarios(cedula)
            flash('Usuario encontrado.', 'success')
        except Exception as e:
            flash(f'Error al buscar usuario: {str(e)}', 'danger')
    
    return render_template('buscar.html', usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True)
