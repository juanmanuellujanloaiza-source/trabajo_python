# Escribe un programa que presente un menú con opciones 
# para realizar una operación matemática (suma, resta, multiplicación o división) 
# entre dos números. El programa debe repetirse hasta que el usuario elija salir.
while True : 
     print("---\n MENU DE OPCIONES---")
     print("1.multiplicar")
     print("2.resta")
     print("3.suma")
     print("4.dividir")
     print("5.salir")
     opcion = input("elige una opcvion (1-5):")

     if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("El resultado de la suma es:", a + b)

     elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("El resultado de la resta es:", a - b)

     elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("El resultado de la multiplicación es:", a * b)

     elif opcion == "4":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        if b != 0:
          print("El resultado de la división es:", a / b)
        
        else:
         print("Error: no se puede dividir entre cero.")

     elif opcion == "5":
        print("¡Hasta luego!")
        break  # rompe el ciclo y termina el programa

     else:
        print("Opción inválida. Intenta de nuevo.")

    







