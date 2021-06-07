#             GLASS BOX TEST (Caja de cristal)
# Se basan en el flujo del programa
# probar todos los caminos posibles de una funsion (ramificaciones, bucles, recursion ,while,......)
# Regresion Testink¿g o mocks (Bugs cuando el programa esta en produccion)
import unittest

def mayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False


class GlassTest(unittest.TestCase):
    
    def testMayorDeEdad(self):
        edad = 20
        resultado = mayorDeEdad(edad)
        self.assertEqual(resultado,True)

    def testMenorDeEdad(self):
        edad = 15
        resultado = mayorDeEdad(edad)
        self.assertEqual(resultado,False)
        





if __name__ == '__main__':
    unittest.main()
