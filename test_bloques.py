import unittest
from procesador_bloques import ordenar_bloques_arreglo

class TestOrdenarBloques(unittest.TestCase):

    def test_ejemplo_problema_1(self):
        # Para el arreglo: (1,3,2,0,7,8,1,3,0,6,7,1) la respuesta esperada es: 123 1378 167
        arr = (1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1)
        esperado = "123 1378 167"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

    def test_ejemplo_problema_2(self):
        # Para (2,1,0,0,3,4) se imprimiría: 12 X 34
        arr = (2, 1, 0, 0, 3, 4)
        esperado = "12 X 34"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

    def test_ceros_intermedios_y_extremos(self):
        # Para (0, 1, 2, 0)
        arr = (0, 1, 2, 0)
        esperado = "X 12 X"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

    def test_arreglo_vacio(self):
        # Para ()
        arr = ()
        esperado = "X"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

    def test_un_solo_cero(self):
        # Para (0,)
        arr = (0,)
        esperado = "X X"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

    def test_sin_ceros(self):
        # Para (5, 4, 3, 2, 1)
        arr = (5, 4, 3, 2, 1)
        esperado = "12345"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

    def test_multiples_ceros_consecutivos(self):
        # Para (0,0,0)
        arr = (0,0,0)
        esperado = "X X X X"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)
        
    def test_arreglo_con_un_solo_numero(self):
        arr = (5,)
        esperado = "5"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

    def test_arreglo_termina_con_cero(self):
        arr = (1,2,3,0)
        esperado = "123 X"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

    def test_arreglo_inicia_con_cero(self):
        arr = (0,4,5,6)
        esperado = "X 456"
        self.assertEqual(ordenar_bloques_arreglo(arr), esperado)

if __name__ == '__main__':
    unittest.main()