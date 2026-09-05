
# Ejercicio 13

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntaje_mas_alto = max(puntajes)
puntaje_mas_bajo = min(puntajes)

print (f"El puntaje mas alto es:{puntaje_mas_alto}")
print (f"El puntaje mas bajo es:{puntaje_mas_bajo}")
print ("Ranking")

descendente = sorted(puntajes, reverse=True)
for numeros in descendente:
    print (numeros)

posicion = descendente.index(990)
print(f"El puntaje 990 esta en la posicion: {posicion +1}")




