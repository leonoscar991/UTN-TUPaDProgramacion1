

# Ejericio 1


lista_notas=[6,4,9,2,8,6,10,8,9,10]


for nota in lista_notas:
        print(nota)

cantidad_notas = len(lista_notas)
suma_notas = sum(lista_notas)
promedio_notas = suma_notas / cantidad_notas
mayor_nota = max(lista_notas)
menor_nota = min(lista_notas)


print(f"El promedio de notas es: {promedio_notas}")

print (f"La nota mas alta es: {mayor_nota}")
print (f"La nota mas baja es: {menor_nota}")
