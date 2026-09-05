
# Ejercicio 4

# Lista de datos repetidos

lista_original = [1,3,5,3,7,1,9,5,3]
lista_sin_repetidos = []

# Recorre la lista original y si el número no esta en la lista_sin_repetidos  lo agrega a la lista_sin_repetidos. 
for numero in lista_original:
    if numero not in lista_sin_repetidos:
        lista_sin_repetidos.append(numero)

# Imprime la lista original.
for numero in lista_original:
    print(numero)

print("/////////////////")

# Imprime la lista sin repetidos.
for numero in lista_sin_repetidos:
    print(numero)    