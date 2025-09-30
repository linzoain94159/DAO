from empleados import Obrero, Administrativo, Vendedor

def str_to_bool(s):
    return s.lower() == 'true'

def cargar_Empleados(ruta):
    empleados = []
    try:
        with open(ruta) as archivo:
            for linea in archivo.readlines():
                datos = linea.strip("\n").split(";")
                if datos[0] == "1":
                    empleado = Obrero(datos[0], datos[1], datos[2], datos[3], float(datos[4]), int(datos[5]))
                elif datos[0] == "2":
                    empleado = Administrativo(datos[0], datos[1], datos[2], datos[3], float(datos[4]), str_to_bool(datos[5]))
                elif datos[0] == "3":
                    empleado = Vendedor(datos[0], datos[1], datos[2], datos[3], float(datos[4]), float(datos[5]))
                empleados.append(empleado)
        return empleados
                
                
    except FileNotFoundError:
        print(f"Error: El archivo en la ruta '{ruta}' no fue encontrado.")
    except IOError:
        print(f"Error: No se pudo leer el archivo en la ruta '{ruta}'.")

def calcular_total(empleados):
    total = 0
    for empleado in empleados:
        total += empleado.calcular_sueldo()
    print(f"El total a pagar en sueldos es: {total}")

def empleados_tipo(empleados):
    tipos = {"1": "Obrero", "2": "Administrativo", "3": "Vendedor"}
    conteo = {"1": 0, "2": 0, "3": 0}
    for empleado in empleados:
        conteo[empleado.tipo] += 1
    for tipo, cantidad in conteo.items():
        print(f"Cantidad de empleados tipo {tipos[tipo]}: {cantidad}")

def empleado_legajo(empleados):
    legajo = input("Ingrese el legajo del empleado: ")
    for empleado in empleados:
        if empleado.legajo == legajo:
            print(f"Sueldo del empleado con legajo {legajo}: {empleado.calcular_sueldo()}")
            return
    print(f"No se encontró un empleado con legajo {legajo}.")


def principal():
    ruta = "DAO\empleados\empleados.csv"
    empleados = cargar_Empleados(ruta)
    opcion = 0
    
    while opcion != 5:
        print("___Menu___ \n"
            "1- Mostrar todos los empleados \n"
            "2- Calcular total a pagar en sueldos \n"
            "3- Contar cantidad de empleados por tipo \n"
            "4- Mostrar sueldo de un empleado por legajo \n"
            "5- Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            for empleado in empleados:
                print(empleado)

        elif opcion == 2:
            calcular_total(empleados)

        elif opcion == 3:
            empleados_tipo(empleados)

        elif opcion == 4:
            empleado_legajo(empleados)

        elif opcion == 5:
            print("Saliendo...")

    

if __name__ == "__main__":
    principal()