# Capture el peso y la altura de una persona, calcule el IMC y 
# determine si dicha persona está en sobrepeso, peso normal o desnutrición.
peso = float(input("ingresar peso:"))
altura = float(input("ingresar altura:"))
IMT = peso/altura**2

if IMT <= 18.5:
    print(f"tiene desnutricion")

elif 18.5 < IMT <= 24.5:
    print(f"tiene peso normal")
elif 25 < IMT <= 30:
    print(f"tiene sobrepeso")
    
else:
    print(f"tiene obesidad")



