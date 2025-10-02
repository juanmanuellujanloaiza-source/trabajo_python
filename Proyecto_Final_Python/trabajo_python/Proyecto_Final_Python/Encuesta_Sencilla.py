#ENCUESTA SENCILLA EN PYTHON

#Tupla con las preguntas de la encuesta (no cambia → tupla es inmutable)
preguntas = (
    "¿Cuál es tu nombre?",
    "¿Cuántos años tienes?",
    "¿Cuál es tu ciudad?",
    "¿Te gusta la programación? (sí/no)"
)

#Lista vacía para almacenar todas las encuestas
encuestas = []

#Preguntamos cuántas personas queremos encuestar
num_personas = int(input("¿Cuántas personas quieres encuestar? "))

#CICLO: Repetimos la encuesta tantas veces como personas haya
for i in range(num_personas):
    print(f"\n--- Encuesta #{i+1} ---")
    
#Diccionario para guardar las respuestas de UNA persona
    encuesta = {}
    
#CICLO: recorremos la tupla de preguntas
    for j, pregunta in enumerate(preguntas):
        respuesta = input(pregunta + " ")
        
#CONDICIONAL: si la pregunta es la edad, convertir a número
        if j == 1:
            respuesta = int(respuesta)
        
        # Guardamos la respuesta en el diccionario
        encuesta[pregunta] = respuesta
    
#CONDICIONAL extra: mensaje si es menor de edad
    if encuesta["¿Cuántos años tienes?"] < 18:
        print("⚠️ Nota: eres menor de edad.")
    
#Agregamos el diccionario a la lista
    encuestas.append(encuesta)

#Mostrar todas las encuestas al final
print("\n===== RESULTADOS FINALES =====")
for i, encuesta in enumerate(encuestas, start=1):
    print(f"\nEncuesta #{i}")
    for clave, valor in encuesta.items():
        print(f"{clave}: {valor}")

#Guardar en un archivo de texto
with open("resultados_encuesta.txt", "w", encoding="utf-8") as archivo:
    archivo.write("===== RESULTADOS DE LAS ENCUESTAS =====\n")
    for i, encuesta in enumerate(encuestas, start=1):
        archivo.write(f"\nEncuesta #{i}\n")
        for clave, valor in encuesta.items():
            archivo.write(f"{clave}: {valor}\n")

print("\n✅ Los resultados se han guardado en 'resultados_encuesta.txt'")
