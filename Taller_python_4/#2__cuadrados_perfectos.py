#Cuadrados perfectos: El programa pide un número n y 
#muestra el cuadrado de cada número entre 1
#y n. Si el cuadrado es par, agregar la nota '(par)

numero = int(input("ingrese un numero:"))

for i in range (1,numero +1): #"i" toma el lugar de numero funciona como contador
    cuadrado = i ** 2  #se calcula "i" por el doble de su valor

    if  cuadrado % 2 == 0: #usamos condicional para determinar si es igual a cero
        print(f"{cuadrado} (par)")

    else :
        print(cuadrado)

    

