import random
random.seed(1)

rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18,
         19, 21, 23, 25, 27, 30, 32, 34, 36]
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17,
          20, 22, 24, 26, 28, 29, 31, 33, 35]



pares = impares = doc1 = doc2 = doc3 = ceros = cant_rojos = cant_negros = 0

for _ in range(1000):
    numero = random.randint(0, 36)  
    
    if numero == 0:
        ceros += 1
    elif numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if 1 <= numero <= 12:
        doc1 += 1
    elif 13 <= numero <=24:
        doc2 += 1
    elif 25 <= numero <= 36:
        doc3 += 1

    if numero in rojos:
        cant_rojos += 1
    elif numero in negros:
        cant_negros += 1

porc = ceros / 1000 * 100
print("cantidad de pares: ", pares)
print("cantidad de impares: ", impares)
print("cantidad de primera docena: ", doc1)
print("cantidad de segunda docena: ", doc2)
print("cantidad de tercera docena: ", doc3)
print("porcentajes de ceros: ", porc)
print("cantidad de rojos: ", cant_rojos)
print("cantidad de negros", cant_negros)
