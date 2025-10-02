#2.Dada una lista con elementos repetidos, escribe un programa que elimine los 
#elementos duplicados y devuelva una lista con solo elementos únicos.


elementos = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unicos = []
for elemento in elementos:
    if elemento not in unicos:
        unicos.append(elemento)
print("Lista sin duplicados:", unicos)