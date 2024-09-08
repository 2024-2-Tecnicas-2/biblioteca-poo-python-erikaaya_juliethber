import unittest
from revista import Revista

class TestRevista(unittest.TestCase):
    def setUp(self):
        self.revista = Revista("National Geographic", 2024, 2024, "Revista de Naturaleza")

    def test_get_titulo(self):
        self.assertEqual(self.revista.titulo, "National Geographic")

    def test_get_anio_publicacion(self):
        self.assertEqual(self.revista.anio_publicacion, 2024)

    def test_get_num_revista(self):
        self.assertEqual(self.revista.num_revista, 2024)

    def test_get_nombre_revista(self):
        self.assertEqual(self.revista.nombre_revista, "Revista de Naturaleza")

if __name__ == '__main__':
    unittest.main()