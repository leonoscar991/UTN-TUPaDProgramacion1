
# Ejercicio 10

# 4 productos 7 dias de la semana.
ventas = [[12, 8, 15, 10, 7, 20, 14],[5, 9, 6, 11, 8, 13, 7],[20, 18, 25, 22, 19, 30, 24],[3, 5, 2, 6, 4, 8, 5]]

mayor_total = 0
mejor_producto = 0
numero_producto = 1

for producto in ventas:
    total = sum(producto)
    print(f"Producto {numero_producto}: {total} unidades")

    if total > mayor_total:
        mayor_total = total
        mejor_producto = numero_producto

    numero_producto = numero_producto + 1
print(f"Producto mas vendido: producto {mejor_producto} con {mayor_total} unidades")

mayor_venta = 0
mejor_dia = 0

for dia in range(7):
    total_dia = 0
    for producto in ventas:
        total_dia = total_dia + producto[dia]
    
    if total_dia > mayor_venta:
        mayor_venta = total_dia
        mejor_dia = dia + 1

print(f"Dia con mayores ventas: dia {mejor_dia} con {mayor_venta} unidades")
