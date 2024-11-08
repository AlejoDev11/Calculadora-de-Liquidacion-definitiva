import sys 
sys.path.append("src")
from controller.controlador import * 
from Logica.calculadora import Usuario
import unittest


class Testcontroller(unittest.TestCase):
    """ Pruebas a la Clase Controlador de la aplicación """

    def setUp(self):
        """ Se ejecuta siempre antes de cada metodo de prueba """
        print("Invocando setUp")
        BorrarFilas() # Asegura que antes de cada metodo de prueba, se borren todos los datos de la tabla

    def setUpClass():
        """ Se ejecuta al inicio de todas las pruebas """
        print("Invocando setUpClass")
        CrearTabla()  # Asegura que al inicio de las pruebas, la tabla este creada
    
    def tearDown(self):
        """ Se ejecuta al final de cada test """
        print("Invocando tearDown")

    def tearDownClass():
        """ Se ejecuta al final de todos los tests """
        print("Invocando tearDownClass")

    def TestInsertCorrecto(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """

        print("Ejecutando testInsert1")
        
        usuario_prueba = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario_prueba)

        Usuario_buscado = BuscarUsuarios(usuario_prueba.cedula)

        self.assertEqual(usuario_prueba.cedula, str(Usuario_buscado.cedula))
        self.assertEqual(usuario_prueba.nombre, str(Usuario_buscado.nombre))
        self.assertEqual(usuario_prueba.salario_basico, str(Usuario_buscado.salario_basico))
        self.assertEqual(usuario_prueba.fecha_inicio, str(Usuario_buscado.fecha_inicio))
        self.assertEqual(usuario_prueba.fecha_ultimo_vacaciones, str(Usuario_buscado.fecha_ultimo_vacaciones))
        self.assertEqual(usuario_prueba.dias_vacaciones_acumulados, str(Usuario_buscado.dias_vacaciones_acumulados))
        
    def TestInsertError(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """

        print("Ejecutando testInsert1")
        
        usuario_prueba = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario_prueba)

        usuario_prueba2 = Usuario("12345","Jose", 4000000, "10/05/2023", "10/05/2024", 160)
        
        with self.assertRaises(ErrorNoInsertado):
            Insertar(usuario_prueba2)
        

if __name__ == '__main__':
    unittest.main()