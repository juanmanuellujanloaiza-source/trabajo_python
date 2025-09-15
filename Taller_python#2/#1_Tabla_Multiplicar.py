#1.Escribe un programa que pida un número entero y
#muestre su tabla de multiplicar del 1 al 10.

numero = int(input("ingrese un numero entero:"))

for i in range (1,11):

  resultado = numero*i

  print(numero, "x" , i , "=" , resultado)
