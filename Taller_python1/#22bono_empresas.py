#Una empresa decide otorgar un bono de temporada a sus empleados de la siguiente manera:
#A empleados que sean estrato 1 les dará un 35% extra sobre su salario
#A empleados que sean estrato 2 les dará un 30% extra sobre su salario 
#A empleados que sean estrato 3 les dará un 25% extra sobre su salario
#A empleados que sean estrato 4 les dará un 20% extra sobre su salario
#A empleados que sean estrato 5 y 6 les dará un 10% extra sobre su salario.
#Elabore un algoritmo que calcule el bono y el total a pagar.

salario = float(input("ingrese salario"))
estracto = float(input("ingrese el estracto:"))
bono = salario*porcentaje
if salario + bono