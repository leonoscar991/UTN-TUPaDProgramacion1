
# Ejercicio 12

numeros = []

for i in range(8):
    entrada = input("Ingrese un número entero: ").strip()
    while not entrada.isdigit():
        print("No es un número entero. Intente de nuevo.")
        entrada = input("Ingrese un número entero: ").strip()
    numeros.append(int(entrada))

ascendente = sorted(numeros)
descendente = sorted(numeros, reverse=True)

print("Lista original:")
for numero in numeros:
    print(numero)

print("Lista de menor a mayor:")
for numero in ascendente:
    print(numero)

print("Lista de mayor a menor:")
for numero in descendente:
    print(numero)