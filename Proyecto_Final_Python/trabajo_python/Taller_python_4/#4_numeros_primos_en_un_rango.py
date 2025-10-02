#Números primos en un rango: El usuario ingresa un número límite y 
#el programa imprime todos los números primos entre 1 y ese límite.

#Pedimos el número límite al usuario
limite = int(input("Ingrese el número límite: "))

# Recorremos cada número desde 2 hasta el límite
for numero in range(2, limite + 1): #El primer for solo sirve para recorrer números
    es_primo = True   # asumimos que el número es primo

    #Revisamos si tiene divisores
    for i in range(2, numero):#El segundo for prueba si cumplen una condición
        if numero % i == 0:   # si encontramos un divisor
            es_primo = False  # ya no es primo
            break             # no seguimos revisando

    #Si sigue siendo primo, lo mostramos
    if es_primo:
        print(numero)