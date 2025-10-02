#Contador de letras específicas: El usuario ingresa una palabra y 
# una letra. El programa recorre la
#palabra y cuenta cuántas veces aparece esa letra. 
#Si la letra no aparece, mostrar un mensaje indicándolo.

palabra = input("ingrese una palabra:")

letra = input("ingrese una letra:")

#contador debe empezar en cero
contador = 0

#Recorremos cada letra de la palabra
for caracter in palabra:
    if caracter == letra:   # Si la letra actual es igual a la buscada
    # este if se usa para recoorrer la palabra
        contador += 1       # Aumentamos el contador

#Revisamos el resultado
if contador > 0:
    # se usa para determinar el resultado
    print(f"La letra '{letra}' aparece {contador} veces en la palabra '{palabra}'.")
else:
    print(f"La letra '{letra}' no aparece en la palabra '{palabra}'.")
