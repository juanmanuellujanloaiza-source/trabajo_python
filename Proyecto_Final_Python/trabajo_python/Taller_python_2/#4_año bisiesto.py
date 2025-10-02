#4.Escribe un programa que pida un año y determine si es un año bisiesto 
#o no. (Un año es bisiesto si es divisible por 4, pero no por 100, 
#a menos que también sea divisible por 400).
anio = int(input("Ingresa un año: "))

if anio % 400 == 0:
    print("El año", anio, "es bisiesto.")
elif anio % 100 == 0:
    print("El año", anio, "NO es bisiesto.")
elif anio % 4 == 0:
    print("El año", anio, "es bisiesto.")
else:
    print("El año", anio, "NO es bisiesto.")
