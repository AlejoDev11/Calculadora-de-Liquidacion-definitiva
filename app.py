import sys 
sys.path.append("src")

from flask import Flask, render_template, request, redirect, url_for, flash
from src.Logica.calculadora import Usuario, CalculadorLiquidacion
import psycopg2
from src import SecretConfig
from controller.controlador import Insertar, Actualizar, Borrar, BuscarUsuarios

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insertar', methods=['GET', 'POST'])
def insertar_usuario():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        basic_salary = request.form['basic_salary']
        start_date = request.form['start_date']
        last_vacation_date = request.form['last_vacation_date']
        accumulated_vacation_days = request.form['accumulated_vacation_days']

        usuario = Usuario(cedula, nombre, basic_salary, start_date, last_vacation_date, accumulated_vacation_days)
        
        try:
            Insertar(usuario)
            flash('Usuario insertado exitosamente.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(str(e), 'danger')

    return render_template('insertar.html')


@app.route('/actualizar', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == 'POST':
        # Capturar los datos del formulario
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        basic_salary = request.form['basic_salary']
        start_date = request.form['start_date']
        last_vacation_date = request.form['last_vacation_date']
        accumulated_vacation_days = request.form['accumulated_vacation_days']

        # Crear un objeto Usuario con los datos capturados
        usuario = Usuario(cedula, nombre, basic_salary, start_date, last_vacation_date, accumulated_vacation_days)

        try:
            # Intentar actualizar el usuario en la base de datos
            Actualizar(usuario)
            flash('Usuario actualizado exitosamente.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            # Mostrar un mensaje de error si algo falla
            flash(str(e), 'danger')

    return render_template('actualizar.html')


@app.route('/borrar', methods=['GET', 'POST'])
def borrar_usuario():
    if request.method == 'POST':
        cedula = request.form['cedula']
        try:
            Borrar(cedula)
            flash('Usuario borrado exitosamente.', 'success')
        except Exception as e:
            flash(str(e), 'danger')
    
    return render_template('borrar.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_usuario():
    usuario = None
    if request.method == 'POST':
        cedula = request.form['cedula']
        try:
            usuario = BuscarUsuarios(cedula)
        except Exception as e:
            flash(str(e), 'danger')

    return render_template('buscar.html', usuario=usuario)

@app.route('/calcular_liquidacion', methods=['GET', 'POST'])
def calcular_liquidacion():
    resultado = None
    if request.method == 'POST':
        cedula = request.form['cedula']
        
        try:
            # Obtener usuario desde la base de datos
            usuario = BuscarUsuarios(cedula)  # Asegúrate de que este método cargue un objeto Usuario válido
            calculador = CalculadorLiquidacion(usuario)
            resultado = calculador.calcular_resultados()

            flash('Cálculo de liquidación realizado exitosamente.', 'success')
        except Exception as e:
            flash(str(e), 'danger')

    return render_template('calcular_liquidacion.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
