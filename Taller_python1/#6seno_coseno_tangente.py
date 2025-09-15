#Cree un programa que pida un ángulo y 
#regrese el seno, el coseno y la tangente del mismo. Pista: use la clase “math”.
import math
angulo = float(input("ingrese un angulo en grados:"))
radianes = math.radians(angulo)

# 4. Calcular seno, coseno y tangente
seno = math.sin(radianes)
coseno = math.cos(radianes)
tangente = math.tan(radianes)

# 5. Mostrar resultados
print(f"Seno de {angulo}° = {seno}")
print(f"Coseno de {angulo}° = {coseno}")
print(f"Tangente de {angulo}° = {tangente}")

