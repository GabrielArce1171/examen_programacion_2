from ejercicio2 import Operacion, Resta

if __name__ == "__main__":
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    suma = Operacion(numero1, numero2)
    resta = Resta(numero1, numero2)

    print(f"La suma de {numero1} y {numero2} es: {suma.calcular()}")
    print(f"La resta de {numero1} y {numero2} es: {resta.calcular()}")