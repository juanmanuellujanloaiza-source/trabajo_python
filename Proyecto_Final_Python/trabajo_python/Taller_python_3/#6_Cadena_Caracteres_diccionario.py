#6.Dado un texto (cadena de caracteres), 
#escribe un programa que cuente la cantidad de veces que aparece cada palabra 
#en el texto y almacene los resultados en un diccionario.

texto = "hola mundo hola python hola programación"
palabras = texto.split()
contador = {}
for palabra in palabras: 
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Conteo de palabras:", contador)
