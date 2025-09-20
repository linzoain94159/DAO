import random
random.seed()

def bajo_cero(temperaturas):
    cantidad = 0
    for i in range(len(temperaturas)):
        if temperaturas[i] < 0:
            cantidad += 1

    print("- La cantidad de dias que la temperatura fue bajo cero: ", cantidad)

def promedio(temperaturas):
    total = 0
    for i in range(len(temperaturas)):
        total += temperaturas[i]
    
    return total / len(temperaturas)

def promedio_calido(temperaturas):
    cantidad = total = 0
    for i in range(len(temperaturas)):
        if temperaturas[i] > 20:
            cantidad += 1
            total += temperaturas[i]

    print("- El promedio de los dias calidos es: ", total / cantidad)

def mas_de_40(temperaturas):
    mas = False
    for i in range(len(temperaturas)):
        if temperaturas[i] > 40:
            mas = True

    if mas:
        print("- Si hay una temperatura arriba de 40")
    else:
        print("- No hay una temperatura arriba de 40")

def mayor_no_calidos(temperaturas):
    mayor = 0
    for i in range(len(temperaturas)):
        if i == 0 and temperaturas[i] <= 20:
            mayor = temperaturas[i]
        else:
            if 20 >= temperaturas[i] > mayor:
                mayor = temperaturas[i]

    print("- La temperatura mas alta de los dias no calidos es: ", mayor)

def cantidad_menor_promedio(temperaturas):
    prom = promedio(temperaturas)
    cantidad = 0
    for i in range(len(temperaturas)):
        if temperaturas[i] < prom:
            cantidad += 1

    print("- La cantidad de dias con temperaturas menor a la promedio es: ", cantidad)


temperaturas = [0] * 5
for i in range(len(temperaturas)):
    temperaturas[i] = random.randint(-20, 49)
    print(temperaturas[i])
    
bajo_cero(temperaturas)
print("- La temperatura promedio es:", promedio(temperaturas))
promedio_calido(temperaturas)
mas_de_40(temperaturas)
mayor_no_calidos(temperaturas)
cantidad_menor_promedio(temperaturas)