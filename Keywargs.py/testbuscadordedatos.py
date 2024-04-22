import unittest
from Buscador_de_datos import buscar_datos

class TestBuscarDatos(unittest.TestCase):

    def setUp(self):
        
        self.database = {
            "persona1": {
                "primer_nombre": "Juan",
                "segundo_nombre": "Pablo",
                "primer_apellido": "Carini",
                "segundo_apellido": "Perez"
            },
            "persona2": {
                "primer_nombre": "Gino",
                "segundo_nombre": "Piero",
                "primer_apellido": "Reginato",
                "segundo_apellido": "Fugazzotto"
            }
        }

    def test_datos_encontrados(self):
        
        resultado = buscar_datos("Juan", "Gino", database=self.database)
        self.assertEqual(resultado, ["Juan", "Gino"])

    def test_datos_no_encontrados(self):
        
        resultado = buscar_datos("Ruiz", "Picasso", database=self.database)
        self.assertEqual(resultado, [])

    def test_datos_mezclados(self):
    
        resultado = buscar_datos("Juan", "Ruiz", "Gino", database=self.database)
        self.assertEqual(resultado, ["Juan", "Gino"])

unittest.main()

