
# Ejercicio 4  “Escape Room: La Bóveda” 

# Nombre del agente (solo letras)
nombre_agente = ""
while not nombre_agente.isalpha():
    nombre_agente = input("Nombre del agente: ")
    if not nombre_agente.isalpha():
        print("Error: Solo se permiten letras")

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzadas_seguidas = 0


bloqueado = False

# Opciones
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    
    # Validación de la opción 
    while True:
        opcion = input("Opcion: ")
        if not opcion.isdigit():
            print("Ingrese un número valido")
        else:
            opcion = int(opcion)         
            if opcion < 1 or opcion > 3:
                print ("Número fuera de rango")
            else:
                break

    if opcion == 1:
        forzadas_seguidas = forzadas_seguidas + 1
        energia = energia - 20
        tiempo = tiempo - 2

        # Riesgo de alarma con poca energía
        if energia < 40:
            print("¡Riesgo de alarma! Elegí un número del 1 al 3")
            numero = ""
            while True:
                numero = input("Número (1-3): ")
                if not numero.isdigit():
                        print("Error: ingrese un número válido")
                else:
                    numero = int(numero)
                    if numero < 1 or numero > 3:
                        print("Error: número fuera de rango")
                    else:
                        break
            if numero == 3:
                alarma = True
                print("¡Se activó la alarma!")

        # Regla anti-spam: 3ra vez seguida forzando
        if forzadas_seguidas == 3:
            alarma = True
            print("La cerradura se trabó. ¡Se activó la alarma!")
        elif not alarma:
            cerraduras_abiertas = cerraduras_abiertas + 1
            print("¡Abriste una cerradura!")

        # Hackear panel
    elif opcion == 2:
        forzadas_seguidas = 0
        energia = energia - 10
        tiempo = tiempo - 3

        for i in range(1, 5):
            codigo_parcial = codigo_parcial + "A"
            print(f"> Paso {i}/4 - Código: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas = cerraduras_abiertas + 1
            print("¡El panel cedió! Se abrió una cerradura.")

    # Descansar
    else:
        forzadas_seguidas = 0
        tiempo = tiempo - 1
        energia = energia + 15
        if energia > 100:
            energia = 100
        if alarma:
            energia = energia - 10
            print("La alarma te mantiene en tensión: -10 de energía extra")
        print(f"Descansaste. Energía: {energia}")


    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        print("\n¡El sistema se bloqueó por la alarma!")

# Fin del juego
if cerraduras_abiertas == 3:
    print(f"\n¡VICTORIA! {nombre_agente} abrió la bóveda.")
elif bloqueado:
    print(f"\nDERROTA. {nombre_agente} quedó atrapado por el bloqueo.")
else:
    print(f"\nDERROTA. {nombre_agente} se quedó sin energía o sin tiempo.")


# fin



