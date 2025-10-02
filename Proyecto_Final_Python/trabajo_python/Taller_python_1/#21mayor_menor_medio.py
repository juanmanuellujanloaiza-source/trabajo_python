# Capture tres números y determine cuál de ellos es el mayor, 
# cual el menor y cuál es el del medio.
num1 = 20
num2 = 45
num3 = 67
if num1 >= num2 and num1 >= num3:
    mayor = num1

elif num2 >= num1 and num2 >= num3:
    mayor = num2

else: 
    mayor = num3

if num1 <= num2 and num1 <= num3:
    menor = num1

elif num2 <= num1 and num2 <= num3:
    menor = num2

else:
     menor = num3
     
medio = (num1+num2+num3) - mayor - menor 

print(f"mayor: {mayor}")
print(f"menor: {menor}")
print(f"medio:{medio}")






     



