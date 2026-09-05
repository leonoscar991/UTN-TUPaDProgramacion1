
# Ejercicio 7

temperaturas = [[5,18],[10,25],[18,34],[4,14],[7,24],[4,26],[11,28]]

# acumuladores.
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0
dia_numero = 1


for dia in temperaturas:
    minima = dia [0]
    maxima = dia [1]

    suma_minimas = suma_minimas + minima
    suma_maximas = suma_maximas + maxima 

    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dia_numero

    print (f"Dia {dia_numero}: minima {minima}, maxima {maxima}")
    dia_numero = dia_numero +1


promedio_minimas = suma_minimas / 7
promedio_maximas = suma_maximas / 7

print(f"Promedio de minimas: {round(promedio_minimas,2)}")

print(f"Promedio de maximas: {round(promedio_maximas,2)}")

print(f"Mayor amplitud termica: dia {dia_mayor_amplitud} con {mayor_amplitud} grados ")
