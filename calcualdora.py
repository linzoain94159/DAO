operaciones = {
    1: lambda x, y: x + y,
    2: lambda x, y: x - y,
    3: lambda x, y: x * y,
    4: lambda x, y: x / y if y != 0 else "Error: División por cero"
}

def calculadora():
    while True:
        opcion = 0
        print("seleccionar opción:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Ingrese opción: ")
        if opcion == "5":
            print("Saliendo...")
            break
        if opcion == "1":
            x = int(input("Ingrese primer número: "))
            y = int(input("Ingrese segundo número: "))
            print(f"Resultado: {operaciones[1](x, y)}")
        elif opcion == "2":
            x = int(input("Ingrese primer número: "))
            y = int(input("Ingrese segundo número: "))
            print(f"Resultado: {operaciones[2](x, y)}")
        elif opcion == "3":
            x = int(input("Ingrese primer número: "))
            y = int(input("Ingrese segundo número: "))
            print(f"Resultado: {operaciones[3](x, y)}")
        elif opcion == "4":
            x = int(input("Ingrese primer número: "))
            y = int(input("Ingrese segundo número: "))
            print(f"Resultado: {operaciones[4](x, y)}")
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    calculadora()