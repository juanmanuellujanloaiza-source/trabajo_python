import re

preguntas = (
    "¿Cuál es tu nombre?",
    "¿Cuántos años tienes?",
    "¿Cuál es tu ciudad?",
    "¿Te gusta la programación? (sí/no)"
)

encuestas = []

# Validar número de personas
while True:
    try:
        num_personas = int(input("¿Cuántas personas quieres encuestar? ").strip())
        if num_personas > 0:
            break
        print("❌ Debe ser mayor que 0.")
    except ValueError:
        print("❌ Ingresa un número válido.")

# Repetir encuesta
for i in range(1, num_personas + 1):
    print(f"\n--- Encuesta #{i} ---")
    encuesta, es_menor = {}, False

    for j, pregunta in enumerate(preguntas):
        while True:
            respuesta = input(pregunta + " ").strip()

            if j in [0, 2]:  # Nombre / Ciudad
                if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$", respuesta):
                    encuesta[pregunta] = respuesta
                    break
                print("❌ Solo letras y espacios.")

            elif j == 1:  # Edad
                try:
                    edad = int(respuesta)
                    if edad < 0:
                        print("❌ La edad no puede ser negativa.")
                    elif edad < 18:
                        print("⚠️ No se puede encuestar a menores de edad.")
                        es_menor = True
                        break
                    else:
                        encuesta[pregunta] = edad
                        break
                except ValueError:
                    print("❌ Ingresa un número entero.")

            else:  # Programación (sí/no)
                encuesta[pregunta] = respuesta.lower()
                break

        if es_menor: break
    if not es_menor: encuestas.append(encuesta)

# Mostrar resultados
print("\n===== RESULTADOS FINALES =====")
for i, e in enumerate(encuestas, 1):
    print(f"\nEncuesta #{i}")
    for k, v in e.items():
        print(f"{k}: {v}")

# Guardar archivo
with open("resultados_encuesta.txt", "w", encoding="utf-8") as f:
    f.write("===== RESULTADOS DE LAS ENCUESTAS =====\n")
    for i, e in enumerate(encuestas, 1):
        f.write(f"\nEncuesta #{i}\n")
        for k, v in e.items():
            f.write(f"{k}: {v}\n")

print("\n✅ Resultados guardados en 'resultados_encuesta.txt'")
