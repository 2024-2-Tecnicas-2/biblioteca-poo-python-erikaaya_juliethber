import unittest
from publicacion import Publicacion

class TestPublicacion(unittest.TestCase):
    def setUp(self):
        self.publicacion = Publicacion("El Quijote", 1605)

    def test_get_titulo(self):
        self.assertEqual(self.publicacion.titulo, "El Quijote")

    def test_get_anio_publicacion(self):
        self.assertEqual(self.publicacion.anio_publicacion, 1605)

if __name__ == '__main__':
    unittest.main()