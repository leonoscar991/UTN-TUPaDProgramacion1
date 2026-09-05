
# Ejercicio 5

# Lista de alumnos.
lista_alumnos=["Juan","Miguel","Antonio","Mateo","Liam","Lucas","Tomas","Pedro"]

print("Lista de alumnos")

for alumnos in lista_alumnos:
    print(alumnos)

opcion = input("¿Quiere agregar o eliminar un estudiante?: ").strip().lower()

if opcion == "agregar":
    agregar_alumno = input("Agregue el nombre del alumno: ").strip().capitalize()
    lista_alumnos.append(agregar_alumno)

elif opcion == "eliminar":
    eliminar_alumno = input("Agregue el nombre que desea eliminar: ").strip().capitalize()
    if eliminar_alumno in lista_alumnos:
        lista_alumnos.remove(eliminar_alumno)

    else:
        print("El nombre no esta en la lista")

for alumno in lista_alumnos:
    print(alumno)



