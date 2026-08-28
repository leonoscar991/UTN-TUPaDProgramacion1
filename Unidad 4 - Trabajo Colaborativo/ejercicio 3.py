# Ejercicio 3 “Agenda de Turnos con Nombres (sin listas)”

# Nombre del operador
nombre_operador = ""
while not nombre_operador.isalpha():
    nombre_operador = input("Ingrese el nombre del operador: ")
    if not nombre_operador.isalpha():
        print("Error: Solo se permiten letras")

# Turnos (vacío = libre)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

# Menú
while True:
    print("\n1) Reservar  2) Cancelar  3) Ver agenda  4) Resumen  5) Cerrar")
    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número válido")
    else:
        opcion = int(opcion)
        if opcion < 1 or opcion > 5:
            print("Error: opción fuera de rango")

        elif opcion == 1:
            # Elegir día
            dia = ""
            while dia != "1" and dia != "2":
                dia = input("Día (1=Lunes, 2=Martes): ")
                if dia != "1" and dia != "2":
                    print("Error: ingrese 1 o 2")

            # Pedir nombre del paciente
            paciente = ""
            while not paciente.isalpha():
                paciente = input("Nombre del paciente: ")
                if not paciente.isalpha():
                    print("Error: solo se permiten letras")

            if dia == "1":
                # Verificar repetido
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: el paciente ya tiene turno ese día")
                # Buscar primer espacio libre Lunes
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado")
                else:
                    print("No hay turnos disponibles para el Lunes")
            elif dia == "2":
                # Verificar repetido
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: el paciente ya tiene turno ese día")
                # Buscar primer espacio libre Martes
                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado")
                else:
                    print("Error: No hay turnos disponibles para el Martes")

        elif opcion == 2:
            # Elegir día
            dia = ""
            while dia != "1" and dia != "2":
                dia = input("Día (1=Lunes, 2=Martes): ")
                if dia != "1" and dia != "2":
                    print("Error: ingrese 1 o 2")

            # Pedir nombre del paciente
            paciente = ""
            while not paciente.isalpha():
                paciente = input("Nombre del paciente a cancelar: ")
                if not paciente.isalpha():
                    print("Error: solo se permiten letras")

            if dia == "1":
                if paciente == lunes1:
                    lunes1 = ""
                    print("Turno cancelado")
                elif paciente == lunes2:
                    lunes2 = ""
                    print("Turno cancelado")
                elif paciente == lunes3:
                    lunes3 = ""
                    print("Turno cancelado")
                elif paciente == lunes4:
                    lunes4 = ""
                    print("Turno cancelado")
                else:
                    print("El paciente no tiene turno ese día")
            elif dia == "2":
                if paciente == martes1:
                    martes1 = ""
                    print("Turno cancelado")
                elif paciente == martes2:
                    martes2 = ""
                    print("Turno cancelado")
                elif paciente == martes3:
                    martes3 = ""
                    print("Turno cancelado")
                else:
                    print("El paciente no tiene turno ese día")

        elif opcion == 3:
            # Elegir día
            dia = ""
            while dia != "1" and dia != "2":
                dia = input("Día (1=Lunes, 2=Martes): ")
                if dia != "1" and dia != "2":
                    print("Error: ingrese 1 o 2")

            if dia == "1":
                print("\nAgenda del Lunes:")
                # Turno 1
                if lunes1 == "":
                    print("Turno 1: (libre)")
                else:
                    print(f"Turno 1: {lunes1}")
                # Turno 2
                if lunes2 == "":
                    print("Turno 2: (libre)")
                else:
                    print(f"Turno 2: {lunes2}")
                # Turno 3
                if lunes3 == "":
                    print("Turno 3: (libre)")
                else:
                    print(f"Turno 3: {lunes3}")
                # Turno 4
                if lunes4 == "":
                    print("Turno 4: (libre)")
                else:
                    print(f"Turno 4: {lunes4}")
            elif dia == "2":
                print("\nAgenda del Martes:")
                # Turno 1
                if martes1 == "":
                    print("Turno 1: (libre)")
                else:
                    print(f"Turno 1: {martes1}")
                # Turno 2
                if martes2 == "":
                    print("Turno 2: (libre)")
                else:
                    print(f"Turno 2: {martes2}")
                # Turno 3
                if martes3 == "":
                    print("Turno 3: (libre)")
                else:
                    print(f"Turno 3: {martes3}")

        elif opcion == 4:
            # Contar turnos ocupados del Lunes
            ocupados_lunes = 0
            if lunes1 != "":
                ocupados_lunes = ocupados_lunes + 1
            if lunes2 != "":
                ocupados_lunes = ocupados_lunes + 1
            if lunes3 != "":
                ocupados_lunes = ocupados_lunes + 1
            if lunes4 != "":
                ocupados_lunes = ocupados_lunes + 1

            # Contar turnos ocupados del Martes
            ocupados_martes = 0
            if martes1 != "":
                ocupados_martes = ocupados_martes + 1
            if martes2 != "":
                ocupados_martes = ocupados_martes + 1
            if martes3 != "":
                ocupados_martes = ocupados_martes + 1

            print(f"\nLunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} disponibles")
            print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} disponibles")

            # Comparar cuál tiene más
            if ocupados_lunes > ocupados_martes:
                print("El Lunes tiene más turnos ocupados")
            elif ocupados_martes > ocupados_lunes:
                print("El Martes tiene más turnos ocupados")
            else:
                print("Empate en turnos ocupados")

        else:
            print("Cerrando sistema...")
            break

# fin
