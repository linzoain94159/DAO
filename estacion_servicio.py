import random


def total_jornada(surtidores):
    tipos = ["Nafta Super", "Nafta Especial", "Gas Oil"]
    total = [0] * 3
    for i in range(len(surtidores)):
        surtidor = surtidores[i]
        total[surtidor[2] - 1] += surtidor[1]
    print("El total de litros vendidos en la jornada, por tipo de combustible es:")
    for i in range(len(total)):
        print(" -", tipos[i], ": ", total[i], "litros")
    print("\n")
        


def menor_consumidor(surtidores):
    menor = []
    for i in range(len(surtidores)):
        surtidor = surtidores[i]
        if i == 0:
            menor = surtidor
        else:
            if surtidor[1] < menor[1]:
                menor = surtidor
    print("El surtidor numero", menor[0], "es el surtidor que menos combustible vendio \n")

def promedio_final(surtidores):
    total = 0
    for i in range(len(surtidores)):
        surtidor = surtidores[i]
        total += surtidor[1]

    print("El porcentaje de venta por surtidor es: ")
    for i in range(len(surtidores)):
        surtidor = surtidores[i]
        print(" - El surtidor numero: ", surtidor[0], "consumio: ", surtidor[1], "litros y reporesenta un: ", surtidor[1] / total * 100, "% del total")


surtidores = [(0, 0, 0)] * 10


for i in range(len(surtidores)):
    surtidores[i] = (random.randint(1, 30), random.randint(0, 1000), random.randint(1, 3))

total_jornada(surtidores)

menor_consumidor(surtidores)

promedio_final(surtidores)
