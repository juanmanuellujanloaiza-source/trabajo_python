preguntas = ( #Tupla
    "¿Cuál es tu nombre?",
    "¿Cuántos años tienes?",
    "¿Cuál es tu ciudad?",
    "¿Te gusta la programación? (sí/no)"
)
encuestas = [] #Lista

num_personas = int(input("¿Cuántas personas quieres encuestar? "))

for i in range(num_personas):
    print(f"\n--- Encuesta #{i+1} ---")

    encuesta = {} #Diccionario

    for j, pregunta in enumerate(preguntas):
        respuesta = input(pregunta + " ")

        if j == 1:
            respuesta = int(respuesta)

        encuesta[pregunta] = respuesta

    if encuesta["¿Cuántos años tienes?"] < 18:
        print(" Nota: eres menor de edad.")

    encuestas.append(encuesta)

    print("\n===== RESULTADOS FINALES =====")
    for i, encuesta in enumerate(encuestas, start=1):
        print(f"\nEncuesta #{i}")
        for clave, valor in encuesta.items():
         print(f"{clave}: {valor}")       

    with open("resultados_encuesta.txt", "w", encoding="utf-8") as archivo:
        archivo.write("===== RESULTADOS DE LAS ENCUESTAS =====\n")
        for i, encuesta in enumerate(encuestas, start=1):
          archivo.write(f"\nEncuesta #{i}\n")
          for clave, valor in encuesta.items():
              archivo.write(f"{clave}: {valor}\n")

print("\n✅ Los resultados se han guardado en 'resultados_encuesta.txt'")




        
