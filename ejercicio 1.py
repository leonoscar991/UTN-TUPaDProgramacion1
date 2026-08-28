
# Ejercicio 1 -  “Caja del Kiosco” 

# Validación del nombre del cliente (solo letras)
nombre_cliente = ""
while not nombre_cliente.isalpha():
    nombre_cliente = input("Ingrese su nombre: ")
    if not nombre_cliente.isalpha():
        print("Error: Solo se permiten letras")

# Validación de la cantidad de productos (entero positivo)
while True:
    cantidad_productos = input("Ingresa la cantidad de productos: ")
    if cantidad_productos.isdigit():
        numero = int(cantidad_productos)
        if numero == 0:
            print("Error: La cantidad de productos no puede ser cero.")
        else:
            cantidad_productos = numero
            break
    else:
        print("Debes ingresar un numero positivo (sin letras ni simbolos)")

# Acumuladores
total_sin_descuento = 0
total_con_descuento = 0

detalle_productos = ""

# Carga de cada producto
for i in range(cantidad_productos):
    print(f"\nProducto {i+1}")

    # Validación del precio
    while True:
        precio = input("Precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error: ingrese un número válido")

    # Validación del descuento
    while True:
        descuento = input("Descuento (S/N): ").upper()
        if descuento == "S" or descuento == "N":
            break
        else:
            print("Error: ingrese S o N")

    # Acumula el precio sin descuento
    total_sin_descuento = total_sin_descuento + precio

    # Aplica el 10% de descuento si corresponde
    if descuento == "S":
        precio_final = precio * 0.9
    else:
        precio_final = precio

    # Acumula el precio final
    total_con_descuento = total_con_descuento + precio_final

    detalle_productos = detalle_productos + f"Producto {i+1} - Precio: ${precio}  Descuento (S/N): {descuento}\n"

# Reporte final
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print(f"\nCliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")
print(detalle_productos)
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")



# fin 