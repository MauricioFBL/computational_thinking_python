#             BLACK BOX TEST (Caja negra)
# Se basan en la especificacion de la función del program
# Mandar inputs y verificar los outpust 
# No hay un orden interno
# Unit testing -> funciones funcionen correctamente de manera individual
# Integration Testing -> Que el conjunto del sobtware o modulo funcione de manera correcta

import unittest
def suma(num_1,num_2):
    return num_1 + num_2

class BlackBoxText(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -17
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -27)

    

if __name__ == '__main__':
    unittest.main()