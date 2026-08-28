

# Ejercicio 2  “Acceso al Campus y Menú Seguro” 

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso_concedido = False

while intentos < 3 and not acceso_concedido:
    intentos = intentos + 1
    print(f"\nIntento {intentos}/3")
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave: ")
    
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not acceso_concedido:
    print("Cuenta bloqueada")

if acceso_concedido:
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")
        
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        else:
            opcion = int(opcion)
            if opcion < 1 or opcion > 4:
                print("Error: opción fuera de rango.")
            elif opcion == 1:
                print("Inscripto")

            elif opcion == 2:
                clave_nueva=input("ingresa nueva clave minimo 6 caracteres: ")
                confirma_clave = input("confirma tu clave: ")
            
                if len (clave_nueva) >= 6 and clave_nueva == confirma_clave:
                    print("cambio de clave exitoso")
                    clave_correcta = clave_nueva
                elif clave_nueva != confirma_clave:
                    print(" Las claves no coinciden, vuelve a ingresar ")
                else:
                    print(" La clave tiene menos de 6 caracteres ")

            
            elif opcion == 3:
                print("¡Seguí adelante, vas muy bien!")
            else:
                print("Saliendo del sistema...")
                break

# fin