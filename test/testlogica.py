import unittest
import sys
sys.path.append("src")
from Logica.calculadora import CalculadorLiquidacion, FloatError
from Logica.calculadora import Usuario
import math

class IndemizacionTest1(unittest.TestCase):
    #En estos test vamos a comprobar las funcionalidades de la clase CalculadorLiquidacion

    #Test correctos

    def testindemnizacion1(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "renuncia"
        Salario_basico = 4000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        diias_vacaciones_acumulados = 15
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, diias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 0
        vacaciones= 166667
        cesantias = 1622223
        primas = 1622223
        intereses_cesantias = 194667
        retencion_en_la_fuente = 360578
        total_a_pagar = 3245200

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion2(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "renuncia"
        Salario_basico = 1000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 0
        vacaciones= 41667
        cesantias = 405556
        primas = 405556
        intereses_cesantias = 48667
        retencion_en_la_fuente = 90145
        total_a_pagar = 811300

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion3(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 1000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 1000000
        vacaciones= 41667
        cesantias = 405556
        primas = 405556
        intereses_cesantias = 48667
        retencion_en_la_fuente = 90145
        total_a_pagar = 1811300

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion4(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 10000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 10000000
        vacaciones= 416667
        cesantias = 4055556
        primas = 4055556
        intereses_cesantias = 486667
        retencion_en_la_fuente = 901445
        total_a_pagar = 18113000

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion5(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 40000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 40000000
        vacaciones= 1666667
        cesantias = 16222223
        primas = 16222223
        intereses_cesantias = 1946667
        retencion_en_la_fuente = 3605778
        total_a_pagar = 72452000

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion6(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 40000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 40000000
        vacaciones= 1666667
        cesantias = 16222223
        primas = 16222223
        intereses_cesantias = 1946667
        retencion_en_la_fuente = 3605778
        total_a_pagar = 72452000

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion7(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 10000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 10000000
        vacaciones= 416667
        cesantias = 4055556
        primas = 4055556
        intereses_cesantias = 486667
        retencion_en_la_fuente = 901445
        total_a_pagar = 18113000

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

        # test Valores Extremos

    def testindemnizacion8(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 1000000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 1000000000
        vacaciones= 41666667
        cesantias = 405555556
        primas = 405555556
        intereses_cesantias = 48666667
        retencion_en_la_fuente = 90144445
        total_a_pagar = 1811300001

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion9(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 1000000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 1000000000
        vacaciones= 41666667
        cesantias = 405555556
        primas = 405555556
        intereses_cesantias = 48666667
        retencion_en_la_fuente = 90144445
        total_a_pagar = 1811300001

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion10(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 1000000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 1000000000
        vacaciones= 41666667
        cesantias = 405555556
        primas = 405555556
        intereses_cesantias = 48666667
        retencion_en_la_fuente = 90144445
        total_a_pagar = 1811300001

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion11(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 0
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 0
        vacaciones= 0
        cesantias = 0
        primas = 0
        intereses_cesantias = 0
        retencion_en_la_fuente = 0
        total_a_pagar = 0

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion12(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 0
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 0
        vacaciones= 0
        cesantias = 0
        primas = 0
        intereses_cesantias = 0
        retencion_en_la_fuente = 0
        total_a_pagar = 0

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

    def testindemnizacion13(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = 1
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 1
        vacaciones= 1
        cesantias = 1
        primas = 1
        intereses_cesantias = 1
        retencion_en_la_fuente = 1
        total_a_pagar = 2

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))
    
        #Test Error
    
    def testindemnizacion14(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = -1
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        with self.assertRaises(FloatError):
            CalculadorLiquidacion(usuario).calcular_resultados()
        


    def testindemnizacion15(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = -10000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        
        with self.assertRaises(FloatError):
            CalculadorLiquidacion(usuario).calcular_resultados()
        

    def testindemnizacion16(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = -500000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)

        with self.assertRaises(FloatError):
            CalculadorLiquidacion(usuario).calcular_resultados()

    def testindemnizacion17(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = -100000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        
        with self.assertRaises(FloatError):
            CalculadorLiquidacion(usuario).calcular_resultados()

    def testindemnizacion18(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = -1
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        
        with self.assertRaises(FloatError):
            CalculadorLiquidacion(usuario).calcular_resultados()

    def testindemnizacion19(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = -12
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        
        with self.assertRaises(FloatError):
            CalculadorLiquidacion(usuario).calcular_resultados()

    def testindemnizacion20(self):
        """
            Verifica la logica del programa
        """
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "Despido"
        Salario_basico = -1
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        dias_vacaciones_acumulados = 18
        #Ejecucion del programa
        usuario = Usuario(cedula, nombre_empleado, Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones, dias_vacaciones_acumulados, motivo_de_finalizacion_contrato)
        
        with self.assertRaises(FloatError):
            CalculadorLiquidacion(usuario).calcular_resultados()

    
if __name__ == '__main__':
    unittest.main()