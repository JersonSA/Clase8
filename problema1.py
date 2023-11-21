def sumar_5_enteros():
    # definicion de variables
    lista = []
    contadorWhile = 0
    tamano = 0
    suma = 0

    # Ingresamos los numeros:
    while contadorWhile < tamano:
        lista.append(int(input("Ingrese numero " + str(contadorWhile+1) + ": ")))
        contadorWhile += 1

    # sumamos los numeros:
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile +=1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero,end=', ')

    print("\nLa suma de todos sus elementos es:")
    print(suma)

