#Clasificación de notas: Un profesor ingresa 5 notas 
#(de 0 a 5). El programa debe mostrar cada nota
#y clasificarla como Aprobada o Reprobada. Al final, 
#mostrar el total de aprobadas y reprobadas.

#Creamos las variables contadoras
aprobadas = 0
reprobadas = 0

#Usamos un ciclo para pedir 5 notas
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))

    #Clasificamos cada nota
    if nota >= 3:
        print(f"Nota {nota} → Aprobada")
        aprobadas += 1   # sumamos al contador de aprobadas
    else:
        print(f"Nota {nota} → Reprobada")
        reprobadas += 1  # sumamos al contador de reprobadas

#Mostramos los resultados finales
print("\nResumen final:")
print(f"Aprobadas: {aprobadas}")
print(f"Reprobadas: {reprobadas}")


     