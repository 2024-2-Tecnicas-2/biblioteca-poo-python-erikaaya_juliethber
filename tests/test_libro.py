import unittest
from biblioteca import Libro  # type: ignore

class TestLibro(unittest.TestCase):

    def test_set_autor(self):
        """Prueba el método set_autor."""
        libro = Libro()
        libro.set_autor("Gabriel García Márquez")
        self.assertEqual(libro.get_autor(), "Gabriel García Márquez", "El autor debería ser 'Gabriel García Márquez'")

    def test_get_numero_de_paginas(self):
        """Prueba el método get_numero_de_paginas."""
        libro = Libro(autor="JK Rowling", numero_de_paginas=450, titulo="Harry Potter", ano_publicacion=1997)
        self.assertEqual(libro.get_numero_de_paginas(), 450, "El número de páginas debería ser 450")

    def test_to_string(self):
        """Prueba el método __str__."""
        libro = Libro(autor="JK Rowling", numero_de_paginas=450, titulo="Harry Potter", ano_publicacion=1997)
        esperado = ("Libro{Titulo=Harry Potter, AnoPublicacion=1997, "
                    "Autor=JK Rowling, NumeroDePaginas=450}")
        self.assertEqual(str(libro), esperado, "El método __str__() no devuelve el valor esperado")

if __name__ == '__main__':
    unittest.main()
