
# Ejercicio 9

tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# Imprime el tablero para guia.
for fila in tablero:
    for casilla in fila:
        print(casilla, end=" ")
    print()


jugador = "X"
jugadas = 0

# Deja hacer 9 jugadas
while jugadas < 9:
    # pide que elija fila y columna.
    fila = int(input("Fila (1 a 3): ")) - 1
    columna = int(input("Columna (1 a 3): ")) - 1
    # valida que la casilla este vacia.
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        # cuenta las jugadas validas.
        jugadas = jugadas + 1
        
        for fila_tablero in tablero:
            for casilla in fila_tablero:
                print(casilla, end=" ")
            print()
        
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
    else:
        print("Casilla ocupada")