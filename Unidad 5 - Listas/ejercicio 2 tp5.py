
# Ejercicio 2

lista_de_productos=[]

for i in range (5):
    #Pide roductos (5) y los agrega a la lista vacia.
    producto = input("Por favor ingresa un producto: ").strip().lower()
    lista_de_productos.append(producto) 

productos_ordenados = sorted(lista_de_productos)

for producto in productos_ordenados:
    print(producto)

eliminar_producto = input("Por favor elija el producto a eliminar: ").strip().lower()

if eliminar_producto in lista_de_productos:
    lista_de_productos.remove(eliminar_producto)
else:
    print("producto a elimar no esta en la lista")

for producto in lista_de_productos:
    print(producto)
