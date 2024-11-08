## Calculadora de Liquidaciones Finales
El proyecto tiene como objetivo desarrollar una aplicación en Python que permita calcular liquidaciones laborales. Esta herramienta facilita la identificación de los diferentes componentes que deben ser pagados a un empleado al finalizar su relación contractual, como indemnización, días de vacaciones no utilizados, intereses de liquidación, bonos por servicio y retenciones fiscales. La aplicación recibe información como el salario base, las fechas de inicio y fin del empleo, y los días de vacaciones acumulados para realizar los cálculos necesarios de acuerdo con las fórmulas y regulaciones actuales.

## Miembros del Equipo
Anderson Monsalve Monsalve
Dubin Andrés Soto Parodi

## Editado por:
Juan Diego Gomez - Juan Diego Usuga

## Editador por segunda vez por:
Alejandro Bustamante y Juan Jose Peñuela 

## Requisitos

Asegúrate de tener instalado:

- Python 3.8 o superior
- `unittest` (incluido por defecto en Python)
 ```markdown
-  pip install psycopg2
  ```
  ```markdown
 - pip install flask
  ```

## Cómo Ejecutar el Proyecto

### Paso 1: Clonar el repositorio

Clona este repositorio en tu máquina local usando Git:
```markdown
https://github.com/AlejoDev11/Calculadora-de-Liquidacion-definitiva/tree/main
```
### Cómo configurar el archivo SecretConfig.py:
Datos secretos que no deben publicarse en el repositorio

Cree un archivo llamado SecretConfig en la carpeta "src" del proyecto, el cual contendrá la información de coneccion con su base de datos.
de esta manera:

Datos secretos que no deben publicarse en el repo

Diligencie estos datos y guarde este archivo como SecretConfig.py en el modulo src
para poder ejecutar la aplicación

#### El Archivo debe de contener lo siguiente:

PGDATABASE = "ESCRIBA EL NOMBRE DE LA BASE DE DATOS"
PGUSER = "ESCRIBA EL USUARIO DE LA DB"
PGPASSWORD = "ESCRIBA LA CONSTRASEÑA"
PGHOST = "ESCRIBA LA DIRECCION DNS O DIRECCION IP DEL SERVIDOR"
PGPORT = 5432 # POR DEFECTO ES 5432, PERO PUEDE CAMBIAR EN SU DB


### Cómo correr las pruebas unitarias del controlador:
```markdown
python test/Controllertest.py
```
### Cómo correr las pruebas unitarias de la logica:
```markdown
python test/testlogica.py
```

### Cómo operar la consola de la BD:
```markdown
python src/Consola/Consola_Base_de_datos.py
```

### Cómo ejecutar la aplicación web:
```markdown
python app.py
```
