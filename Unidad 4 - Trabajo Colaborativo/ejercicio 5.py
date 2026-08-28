
# Ejercicio 5   Escape Room:"La Arena del Gladiador"

# Nombre del Gladiador (solo letras)
nombre_gladiador = ""
while not nombre_gladiador.isalpha():
    nombre_gladiador = input("Nombre del Gladiador: ")
    if not nombre_gladiador.isalpha():
        print("Error: Solo se permiten letras")

# Estadísticas iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
dano_ataque_pesado = 15
dano_enemigo = 12
turno_gladiador = True


print("\n=== INICIO DEL COMBATE ===")


# Opciones
while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    # validación de la opción 
    while True:
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Ingrese un número valido.")
        else:
            opcion = int(opcion)
            if opcion < 1 or opcion > 3:
                print("Error: opción fuera de rango.")
            else:
                break
    # Atáque Pesado
    if opcion == 1:
        if vida_enemigo < 20:
            dano = dano_ataque_pesado * 1.5
            print("¡GOLPE CRÍTICO!") 
        else:
            dano = dano_ataque_pesado
        vida_enemigo = vida_enemigo - dano
        print(f"¡Atacaste al enemigo por {dano:.1f} puntos de daño!")
    # Ráfaga Veloz
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo = vida_enemigo - 5
            print("> Golpe conectado por 5 de daño")
    # Curar
    else:
        if pociones > 0:
            vida_jugador = vida_jugador + 30
            pociones = pociones - 1
            print("Te curaste 30 puntos de vida")
        else:
            print("¡No quedan pociones!")

    # Turno del Enemigo
    vida_jugador = vida_jugador - dano_enemigo
    print(f"¡El enemigo te atacó por {dano_enemigo} puntos de daño!")

# Fin del Juego
if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")

# fin