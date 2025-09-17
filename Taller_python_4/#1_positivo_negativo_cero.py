#Suma de positivos y negativos: El programa pide 5 números enteros al usuario y debe indicar
#cuántos son positivos, cuántos son negativos y cuántos son iguales a cero.

#Inicializamos los contadores en 0
positivos = 0
negativos = 0
ceros = 0

#Usamos un ciclo para pedir 5 números
for i in range(5):
    numero = int(input("Ingresa un número entero: "))

    #Clasificamos el número con condicionales
    if numero > 0:
        positivos += 1   # sumamos 1 al contador de positivos
    elif numero < 0:
        negativos += 1   # sumamos 1 al contador de negativos
    else:
        ceros += 1       # sumamos 1 al contador de ceros

#Mostramos los resultados finales
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
print("Cantidad de ceros:", ceros)