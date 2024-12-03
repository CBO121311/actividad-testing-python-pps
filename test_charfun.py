"""
test_charfun.py

Archivo con pruebas unitarias de la función 'esPalindromo' del módulo 'charfun.py'.
Las pruebas están diseñadas para validar diferentes casos

Ultima Modificación. 04/12/2024

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
        # Un solo carácter
        self.assertEqual(esPalindromo("v"), False)

    def test_palindromos(self):
        # Cadenas palíndromas
        self.assertEqual(esPalindromo("Somos o no somos"), True)
        self.assertEqual(esPalindromo("Luz azul"), True)
        self.assertTrue(esPalindromo("12321"))

    def test_no_palindromos(self):
        # Cadenas no palíndromas
        self.assertEqual(esPalindromo("Gato grande"), False)
        self.assertEqual(esPalindromo("Estudiar mucho"), False)

    def test_cadenas_con_tildes_y_simbolos(self):
        # Cadenas con tildes y caracteres especiales
        self.assertEqual(esPalindromo("¡Abusón, acá no suba!"), True)
        self.assertTrue(esPalindromo("¿A mamá Roma le aviva el amor a mamá?"), True) 
        self.assertTrue(esPalindromo("Sólos"), True) 

if __name__ == "__main__":
    unittest.main()