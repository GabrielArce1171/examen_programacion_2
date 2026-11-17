from ejercicio1 import Estacionamiento

if __name__ == "__main__":
    while True:
        try:
            horas = int(input("Ingrese la cantidad de horas (entero mayor que cero): "))
            if horas > 0:
                break
            else:
                print("Por favor, ingrese un número entero mayor que cero.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    estacionamiento = Estacionamiento(horas)
    estacionamiento.mostrarRecibo()