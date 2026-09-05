
# Ejercicio 6

# Lista original
lista_numeros=[10,20,30,40,50,60,70]

# Lista rotada, se usa slicing: toma el ultimo valor de la cadena y lo concatena como lista con la lista de los numeros que quedan.
lista_rotada = [lista_numeros[-1]] + lista_numeros[:-1]

# Imprime lista original.
print("Lista original:")
for numero in lista_numeros:
    print(numero)
    
# Imprime lista rotada .
print("Lista rotada:")
for numero in lista_rotada:
    print(numero)
