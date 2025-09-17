#7.Dado un diccionario de productos con sus precios, escribe un programa que convierta +
#el diccionario en una lista de tuplas, donde cada tupla contenga el producto y su precio.

productos = {"manzana": 1.5, "pera": 2.0, "plátano": 1.2}
lista_tuplas = list(productos.items())
print("Lista de tuplas:", lista_tuplas)