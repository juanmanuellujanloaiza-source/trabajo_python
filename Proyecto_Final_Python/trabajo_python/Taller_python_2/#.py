#Escribe un programa que pida un número entero positivo n 
#y calcule la suma de todos los números pares entre 1 y n

numero = int(input("ingrese un numero entero positivo:"))

suma= 0

for i in range (1,numero + 1):

 if i % 2 == 0 :
  
  suma += i
  
  print(f"la suma de los numeros pares entre 1", numero , "es:", suma )
