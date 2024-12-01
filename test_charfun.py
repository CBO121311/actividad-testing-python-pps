"""
test_charfun.py

Archivo que contiene un conjunto de pruebas unitarias para verificar el correcto funcionamiento
de la función `esPalindromo`, definida en el módulo `charfun.py`.

Las pruebas están diseñadas para validar diferentes casos, incluyendo:
- Cadenas vacías o con espacios.
- Cadenas de un solo carácter.
- Palíndromos simples y complejos (incluyendo tildes, mayúsculas y símbolos).
- Cadenas que no son palíndromas.

Ultima Modificación. 01/12/2024

Autor. Alejandro López Calderón
"""

import unittest
from charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    def test_cadena_vacia(self):
        # Cadena vacía
        self.assertEqual(esPalindromo(""), False)  

    def test_cadena_espacio(self):
        # Solo espacios
        self.assertEqual(esPalindromo("    "), False)
    
    def test_un_caracter(self):
        # Un solo carácter no debería ser palíndromo
        self.assertEqual(esPalindromo("c"), False)

    def test_palindromos(self):
        # Cadenas palíndromas
        self.assertEqual(esPalindromo("Somos o no somos"), True)
        self.assertEqual(esPalindromo("Luz azul"), True)
        self.assertEqual(esPalindromo("La tele letal"), True)

    def test_no_palindromos(self):
        # Cadenas no palíndromas
        self.assertEqual(esPalindromo("Gato grande"), False)
        self.assertEqual(esPalindromo("Estudiar mucho"), False)

    def test_cadenas_con_tildes_y_simbolos(self):
        # Cadenas con tildes y caracteres especiales
        self.assertTrue(esPalindromo("ÁÉÍÚ úíéá"), True)
        self.assertEqual(esPalindromo("¡Abusón, acá no suba!"), True)
        self.assertTrue(esPalindromo("Sólos"), True) 

if __name__ == "__main__":
    unittest.main()