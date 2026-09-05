
# Ejercicio 3

# Importa libreria random-
import random

# Listas que se van a completar.
numeros_aleatorios = []
lista_num_pares = []
lista_num_impares = []

# Genera 15 numeros aleatorios y los imprime.
for i in range (15):
    numero_random = random.randint(1,100)
    numeros_aleatorios.append(numero_random)
print ("Números generados: ")
for numero in numeros_aleatorios:
    print(numero)

# Compara si el número generado es par o impar.
for numero in numeros_aleatorios:
    if numero % 2 == 0:
        lista_num_pares.append(numero)
    else:
        lista_num_impares.append(numero)

# Imprime los números pares.
print("Números pares:")
for numero in lista_num_pares:
    print(numero)

# Imprime los números impares 
print("Números impares:")
for numero in lista_num_impares:
    print(numero)

# Saca la cantidad de números en cada lista e imprime.
print(f"Cantidad de números pares: {len(lista_num_pares)}")
print(f"Cantidad de números impares: {len(lista_num_impares)}")
