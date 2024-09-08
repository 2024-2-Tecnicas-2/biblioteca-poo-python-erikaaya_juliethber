import unittest
from biblioteca import Publicacion # type: ignore
class TestPublicacion(unittest.TestCase):

    def test_set_titulo(self):
        """Prueba el método set_titulo."""
        publicacion = Publicacion()
        publicacion.set_titulo("Cien años de soledad")
        self.assertEqual(publicacion.get_titulo(), "Cien años de soledad", "El título debería ser 'Cien años de soledad'")

    def test_get_ano_publicacion(self):
        """Prueba el método get_ano_publicacion."""
        publicacion = Publicacion(titulo="Cien años de soledad", ano_publicacion=1967)
        self.assertEqual(publicacion.get_ano_publicacion(), 1967, "El año de publicación debería ser 1967")

    def test_to_string(self):
        """Prueba el método __str__."""
        publicacion = Publicacion(titulo="Cien años de soledad", ano_publicacion=1967)
        esperado = "Publicacion{Titulo=Cien años de soledad, AnoPublicacion=1967}"
        self.assertEqual(str(publicacion), esperado, "El método __str__() no devuelve el valor esperado")

if __name__ == '__main__':
    unittest.main()
