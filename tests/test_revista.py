import sys
import os
import unittest

# Agrega el directorio 'src' a la ruta de Python para que se pueda importar 'Revista'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from biblioteca import Revista  # type: ignore # tipo: ignore

class TestRevista(unittest.TestCase):
    """Pruebas unitarias para la clase Revista."""

    def test_set_numero_revistas(self):
        """Prueba el método set_numero_revistas."""
        revista = Revista()
        revista.set_numero_revistas(20)
        self.assertEqual(revista.get_numero_revistas(), 20, "El número de revistas debería ser 20")

    def test_get_nombre_revista(self):
        """Prueba el método get_nombre_revista."""
        revista = Revista(numero_revistas=10, nombre_revista="National Geographic", titulo="Exploraciones", ano_publicacion=2024)
        self.assertEqual(revista.get_nombre_revista(), "National Geographic", "El nombre de la revista debería ser 'National Geographic'")

    def test_to_string(self):
        """Prueba el método __str__."""
        revista = Revista(numero_revistas=10, nombre_revista="National Geographic", titulo="Exploraciones", ano_publicacion=2024)
        esperado = "Revista{Titulo=Exploraciones, AnoPublicacion=2024, NumeroRevistas=10, NombreRevista=National Geographic}"
        self.assertEqual(str(revista), esperado, "El método __str__() no devuelve el valor esperado")

if __name__ == '__main__':
    unittest.main()
