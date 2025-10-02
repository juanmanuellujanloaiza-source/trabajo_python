# Solicite el ingreso de una palabra y una letra, 
# luego diga en qué posición está la letra que usted indicó.
palabra = input("ingresar palabra:")
letra = input("ingresar letra:")
posicion = palabra.find(letra)
print(f"la posicion de la letra es:{posicion}")

