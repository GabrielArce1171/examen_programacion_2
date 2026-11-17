from Actividad_2 import Rectangulo

if __name__ == "__main__":
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    rectangulo = Rectangulo(base, altura)
    rectangulo.mostrarArea()
