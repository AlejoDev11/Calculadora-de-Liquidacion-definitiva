import sys 
sys.path.append("src")
import unittest
from controller.controlador import BorrarFilas, CrearTabla, Insertar, Actualizar, BuscarUsuarios, Borrar, ErrorNoInsertado, ErrorNoActualizado, ErrorNoEncontrado, ErrorNoBorrado
from Logica.calculadora import Usuario

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

    def testsInsertCorrecto(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """

        print("Ejecutando testInsertCorrecto")
        
        usuario_prueba = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario_prueba)

        Usuario_buscado = BuscarUsuarios(usuario_prueba.cedula)

        self.assertEqual(str(usuario_prueba.cedula), Usuario_buscado.cedula)
        self.assertEqual(str(usuario_prueba.nombre), Usuario_buscado.nombre)
        self.assertEqual(str(usuario_prueba.salario_basico), Usuario_buscado.salario_basico)
        self.assertEqual(str(usuario_prueba.fecha_inicio), Usuario_buscado.fecha_inicio)
        self.assertEqual(str(usuario_prueba.fecha_ultimo_vacaciones), Usuario_buscado.fecha_ultimo_vacaciones)
        self.assertEqual(str(usuario_prueba.dias_vacaciones_acumulados), Usuario_buscado.dias_vacaciones_acumulados)
        
    def testsInsertError(self):
        """ Verifica que funcione bien la excepcion ErrorNoInsertado
            y falla porque intenta insertar 2 usuarios con la misma cedula
        """

        print("Ejecutando testInsertError")
        
        usuario_prueba = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario_prueba)

        usuario_prueba2 = Usuario("12345","Jose", 4000000, "10/05/2023", "10/05/2024", 160)
        
        with self.assertRaises(ErrorNoInsertado):
            Insertar(usuario_prueba2)

    def testActualizarCorrecto(self):
        """
            Verifica que funcione la funcionalidad de Actualizar, con una variable cedula para encontrar el usuario y los datos a actualizar
        """
        print("Ejecutando testActualizarCorrecto")

        usuario = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario)
        #entradas
        usuario_actualizado = Usuario(cedula= "12345", nombre = "Jose", salario_basico = 5000000, fecha_inicio = "10/04/2023", fecha_ultimo_vacaciones = "10/04/2024", dias_vacaciones_acumulados = 159)

        Actualizar(usuario.cedula,usuario_actualizado.nombre, usuario_actualizado.salario_basico, usuario_actualizado.fecha_inicio, usuario_actualizado.fecha_ultimo_vacaciones, usuario_actualizado.dias_vacaciones_acumulados)
        Usuario_buscado = BuscarUsuarios(usuario.cedula)

        self.assertEqual(str(usuario_actualizado.cedula), Usuario_buscado.cedula)
        self.assertEqual(str(usuario_actualizado.nombre), Usuario_buscado.nombre)
        self.assertEqual(str(usuario_actualizado.salario_basico), Usuario_buscado.salario_basico)
        self.assertEqual(str(usuario_actualizado.fecha_inicio), Usuario_buscado.fecha_inicio)
        self.assertEqual(str(usuario_actualizado.fecha_ultimo_vacaciones), Usuario_buscado.fecha_ultimo_vacaciones)
        self.assertEqual(str(usuario_actualizado.dias_vacaciones_acumulados), Usuario_buscado.dias_vacaciones_acumulados)

    def testActualizarError(self):
        """
            Verifica que se genere la excepcion ErrorNoActualizado
            este falla debido a que la cedula no esta asociada a ningun usuario de la tabla
        """
        print("Ejecutando testActualizarError")

        usuario = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario)

        usuario_actualizado = Usuario(cedula= "1235", nombre = "Jose", salario_basico = 5000000, fecha_inicio = "10/04/2023", fecha_ultimo_vacaciones = "10/04/2024", dias_vacaciones_acumulados = 159)

        with self.assertRaises(ErrorNoActualizado):
            Actualizar(usuario_actualizado.cedula, usuario_actualizado.nombre, usuario_actualizado.salario_basico, usuario_actualizado.fecha_inicio, usuario_actualizado.fecha_ultimo_vacaciones, usuario_actualizado.dias_vacaciones_acumulados)

    def testBorrarCorrecto(self):
        """
            Verificar que funcione correctamente la funcionalidad de Borrar()
        """
        print("Ejecutando testBorrarCorrecto")
        
        usuario = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario)

        Borrar(usuario.cedula)

        with self.assertRaises(ErrorNoEncontrado):
            BuscarUsuarios(usuario.cedula)

    def testBorrarError(self):
        """
            Verifica que se genere de manera correcta la excepcion ErrorNoBorrado
            esta se genera debido a que la condicion de busqueda no existe en la tabla
        """
        print("Ejecutando testBorrarError")

        usuario = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario)
        cedula = "hola_mundo"

        with self.assertRaises(ErrorNoBorrado):
            Borrar(cedula)

    def testBuscarCorrecto(self):
        """
            Verifica que funcione la funcionalidad de Buscar
        """
        print("Ejecutando testBuscarCorrecto")

        usuario_prueba = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario_prueba)

        Usuario_buscado = BuscarUsuarios(usuario_prueba.cedula)

        self.assertEqual(str(usuario_prueba.cedula), Usuario_buscado.cedula)
        self.assertEqual(str(usuario_prueba.nombre), Usuario_buscado.nombre)
        self.assertEqual(str(usuario_prueba.salario_basico), Usuario_buscado.salario_basico)
        self.assertEqual(str(usuario_prueba.fecha_inicio), Usuario_buscado.fecha_inicio)
        self.assertEqual(str(usuario_prueba.fecha_ultimo_vacaciones), Usuario_buscado.fecha_ultimo_vacaciones)
        self.assertEqual(str(usuario_prueba.dias_vacaciones_acumulados), Usuario_buscado.dias_vacaciones_acumulados)

    def testBuscarError(self):
        """
            Verifica que se genere de manera correcta la excepcion ErrorNoEncontrado
            esta se da porque la variable que usamos para buscar en la tabla no esta asociada a ninguna fila de la BD
        """
        print("Ejecutando testBuscarError")

        usuario = Usuario("12345","Juan", 2000000, "10/05/2023", "10/05/2024", 150)
        Insertar(usuario)
        cedula = "Hola_Mundo"
        with self.assertRaises(ErrorNoEncontrado):
            BuscarUsuarios(cedula)



if __name__ == '__main__':
    unittest.main()