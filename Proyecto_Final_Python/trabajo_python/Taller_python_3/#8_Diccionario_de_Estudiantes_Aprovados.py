#8.Dado un diccionario con nombres de estudiantes y sus calificaciones, 
#escribe un programa que cree un nuevo diccionario con solo aquellos estudiantes que hayan aprobado
#(nota >= 60).

estudiantes = {"Ana": 85, "Luis": 58, "Pedro": 70, "Sofía": 45, "María": 90}
aprobados = {nombre: nota for nombre, nota in estudiantes.items() if nota >= 60}
print("Estudiantes aprobados:", aprobados)