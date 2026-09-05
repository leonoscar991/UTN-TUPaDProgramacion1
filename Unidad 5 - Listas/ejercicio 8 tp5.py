
# Ejercicio 8

notas = [[4,8,7],[8,7,9],[6,5,7],[8,9,9],[6,8,9]]

numero_alumno = 1
for alumno in notas:
    promedio = sum(alumno) / len(alumno)
    print(f"Promedio alumno {numero_alumno} : {round(promedio,2)}")
    numero_alumno = numero_alumno + 1


for materia in range(3):
    suma=0
    for alumno in notas:
        suma = suma + alumno[materia]
    promedio = suma / 5
    print(f"Promedio materia {materia +1} : {round(promedio,2)}")

    