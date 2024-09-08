from libro import Libro
from revista import Revista

def main():
    # Crear instancias de Libro y Revista
    libro = Libro("El Quijote", 1605, "Miguel de Cervantes", 863)
    revista = Revista("National Geographic", 2023, 500, "National Geographic")

    # Mostrar información
    print("Información del Libro:")
    libro.mostrar_info()

    print("\nInformación de la Revista:")
    revista.mostrar_info()

if __name__ == "__main__":
    main()