"""
CALCULADORA BÁSICA COLABORATIVA
Punto de entrada principal (Gestionado por el Estudiante 1)
"""
from operaciones import sumar, restar, multiplicar, dividir

def mostrar_menu():
    print("\n" + "=" * 30)
    print("      CALCULADORA DE EQUIPO   ")
    print("=" * 30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("=" * 30)

def pedir_numeros():
    try:
        n1 = float(input("Ingresa el primer número: "))
        n2 = float(input("Ingresa el segundo número: "))
        return n1, n2
    except ValueError:
        print("⚠️ Por favor ingresa únicamente valores numéricos.")
        return None, None

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "5":
            print("\n¡Gracias por usar la calculadora! Hasta pronto.")
            break

        if opcion in ["1", "2", "3", "4"]:
            num1, num2 = pedir_numeros()
            if num1 is None or num2 is None:
                continue

            if opcion == "1":
                resultado = sumar(num1, num2)
                print(f"\n✅ Resultado de la Suma: {resultado}")
            elif opcion == "2":
                resultado = restar(num1, num2)
                print(f"\n✅ Resultado de la Resta: {resultado}")
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                print(f"\n✅ Resultado de la Multiplicación: {resultado}")
            elif opcion == "4":
                resultado = dividir(num1, num2)
                print(f"\n✅ Resultado de la División: {resultado}")
        else:
            print("⚠️ Opción inválida. Elige un número del 1 al 5.")

if __name__ == "__main__":
    main()
