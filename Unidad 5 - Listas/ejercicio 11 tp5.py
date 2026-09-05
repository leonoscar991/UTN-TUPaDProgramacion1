
# Ejercicio 11

# Lista de nombres.
nombres = ["Ana", "Bruno", "Carla", "Diego", "Lena", "Facundo", "Gabriela", "Hugo", "Juan", "Carlos"]

# Usuario ingresa el nombre que quiere buscar.
buscar = input("Ingrese el nombre a buscar: ").strip().capitalize()

# En la lista busca el indice y si esta lo imprime.
if buscar in nombres:
    posicion = nombres.index(buscar)
    print(f"{buscar} esta en la lista, en la posicion {posicion}")
else:
    print(f"{buscar} no esta en la lista")


